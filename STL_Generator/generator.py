from data_manager import Import_data


class STL_Generator():
    def __init__(self, file_path):
        self.file_path = file_path
        self.import_data = Import_data()
        self.OBJList = self.import_data.from_excel(self.file_path)[0]
        self.comments = self.import_data.from_excel(self.file_path)[1]

    def CM_BlockGen(self, inputstr, comment=""):
        text = u"""
    NETWORK
    TITLE ="""+inputstr + " " + comment + """
        A "true";
        = %L0.0;
        BLD 103;
        CALL #""" + inputstr + """
        (  AI1_available := %L0.0 , 
            AI_RAW                      := "DB_Input".ai."""+inputstr + """, 
            settings                    := "DB_Settings".Unit_Measurements.EM_InputConditioning."""+inputstr + """, 
            status                      := "DB_Status".Unit_Measurements.EM_InputConditioning."""+inputstr + """, 
            cmd                         := "DB_Cmds".Unit_Measurements.EM_InputConditioning."""+inputstr + """
        );
        NOP 0;
    """
        return text

    def Generate_Block(self):
        startStr = """
        FUNCTION_BLOCK "FB_EM_InputConditioning"
        { S7_Optimized_Access := 'FALSE' }
        VERSION : 0.1
        VAR 
        """
        medStr = """
        END_VAR
        BEGIN
        """
        endStr = """
        END_FUNCTION_BLOCK
        """
        blockText = startStr
        for obj in self.OBJList:
            blockText += obj + """ : "FB_CM_MeasurementPoint";\r\n"""

        blockText += medStr

        # for obj in OBJList:
        for obj in range(len(self.OBJList)):
            blockText += self.CM_BlockGen(
                self.OBJList[obj], "- " + self.comments[obj])

        blockText += endStr

        with open("generated_STL.txt", "w", encoding="utf-8") as f_STL:
            f_STL.write(blockText)
