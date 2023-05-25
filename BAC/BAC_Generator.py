def Generate_BAC_input(localisation, input_dict, template_str):
    Instances_list = []
    for type in input_dict:

        if type == 'AI':
            if template_str == 'MeasurementPoint_002':
                for element in input_dict['AI']:
                    temp_list = [f"GPEC/Gdansk/{localisation}", '/?MeasurementPoint_002?/',
                                 'GPEC/Pomiary//?MeasurementPoint_002?/',
                                 f"ua:SCADA-APP\\\\[KEPServerEX]{localisation.split('/')[1]}/{localisation.split('/')[1]}/{element[3]}.value",
                                 element[4], "", element[1], element[5]]
                    Instances_list.append(temp_list)
        if type == 'DI':
            if template_str == 'DigitalMeasurement':

                for element in input_dict['DI']:
                    temp_list = [f"GPEC/Gdansk/{localisation}", '/?DigitalMeasurement?/', 'GPEC//?DigitalMeasurement?/',
                                 f"ua:SCADA-APP\\\\[KEPServerEX]{localisation.split('/')[1]}/{localisation.split('/')[1]}.{element[3]}",
                                 element[4], element[3]]
                    Instances_list.append(temp_list)

        if type == 'pump':
            if template_str == 'SRU_CM_Pump':
                i = 1
                for element in input_dict['pump']:
                    temp_list = [f"GPEC/Gdansk/{localisation}", '/?SRU_CM_Pump?/', 'GPEC/Napedy//?SRU_CM_Pump?/', '',
                                 element[4], '',
                                 '', '',
                                 f"ua:SCADA-APP\\\\[KEPServerEX]{localisation.split('/')[1]}/{localisation.split('/')[1]}",
                                 '', f"{i}", '', '', '']
                    i += 1
                    Instances_list.append(temp_list)
            elif template_str == 'SPC_Wilenska_Naped':
                pass

        if type == 'valve':
            if template_str == 'SPC_Wilenska_Zawor':
                i = 1
                for element in input_dict['valve']:
                    temp_list = [f"GPEC/Gdansk/{localisation}", '/?SPC_Wilenska_Zawor?/',
                                 'GPEC/Zawory//?SPC_Wilenska_Zawor?/', '', element[4], f"ending_{i}", '',
                                 element[1], '', '']
                    i += 1
                    Instances_list.append(temp_list)
        else:
            pass
    return Instances_list
