import pandas as pd
import shutil
import os

template_prefix = ['TargetEquipment', 'InstanceName', 'EquipmentClass']
templates = {
    "MeasurementPoint_002": template_prefix + ['DataInput_value', 'DESC', 'Display_Name',
                                               'MeasurementPoint_002', 'Unit_value'],
    "DigitalMeasurement": template_prefix + ['DataInput_value', 'DESC', 'DigitalMeasurement'],
    "SRU_CM_Pump": template_prefix + ['cmd_path', 'DESC', 'Dynamics_path',
                                      'ExtraData_path', 'KKS_short', 'main_path', 'PID_path', 'pump_nb',
                                      'Settings_path', 'SRU_CM_Pump', 'Status_path'],
    "SPC_Wilenska_Naped": template_prefix + ['cmd_path', 'DESC', 'Dynamics_path',
                                             'ExtraData_path', 'PID_path', 'pump_nb', 'Settings_path',
                                             'SPC_Wilenska_Naped', 'SPC_Wilenska_Naped_2', 'Status_path', ],
    "SPC_Wilenska_Zawor": template_prefix + ['Cmd_path', 'Desc', 'ending', 'Settings_path', 'SPC_Wilenska_Zawor',
                                             'Status_path', 'Widocznosc_KR', ]
}


def input_handler(file):
    df = pd.read_excel(file, sheet_name="ICO")
    df_for_DI = pd.read_excel(file, sheet_name="IO")
    data_dict = {}
    data_dict = {row['type']: []
                 for index, row in df.iterrows() if row['type'] not in data_dict}
    data_dict['DI'] = []

    for index, row in df.iterrows():
        if 'REZ' not in row['name'].upper():
            row_to_list = list(row)
            data_dict[row['type']].append(row_to_list)

    # Osobna pętla dla sygnałó cyfrowych pobieranych z zakładki IO w excelu

    for index, row in df_for_DI.iterrows():
        if 'REZ' not in row['Nazwa PLC'].upper():
            if row['Typ'] == 'DI':
                row_to_list = list(row)
                data_dict['DI'].append(row_to_list)

    return data_dict


def wrtie_to_excel(input_list, suffix, path=os.getcwd()):
    if len(input_list) > 0:
        clear_files(suffix, path)
        df_input = pd.DataFrame(input_list)
        df_input.columns = templates[input_list[0][1][2:-2]]
        with pd.ExcelWriter(f'BAC_template_{suffix}.xlsx', mode='a', engine='openpyxl',
                            if_sheet_exists='overlay') as writer:
            df_input.to_excel(writer,
                              sheet_name='ClassInstantiation', index=False)


def clear_files(suffix, path):
    src_path = f"{path}\\templates\BAC_template.xlsx"
    dst_path = f"{path}\\BAC_template_{suffix}.xlsx"
    if os.path.exists(dst_path):
        os.remove(dst_path)
    shutil.copy(src_path, dst_path)
