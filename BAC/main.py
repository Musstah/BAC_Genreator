from data_manager import input_handler, wrtie_to_excel
from BAC_Generator import Generate_BAC_input

data_dict = input_handler('SPCHavla2.xlsx')

AI_list = Generate_BAC_input(
    'Poludnie/Super_SPC', data_dict, 'MeasurementPoint_002')
wrtie_to_excel(AI_list, 'AI')

DI_list = Generate_BAC_input(
    'Poludnie/Super_SPC', data_dict, 'DigitalMeasurement')
wrtie_to_excel(DI_list, 'DI')

Pumps_list = Generate_BAC_input(
    'Poludnie/Super_SPC', data_dict, 'SRU_CM_Pump')
wrtie_to_excel(Pumps_list, 'Pumps')

Valves_list = Generate_BAC_input(
    'Poludnie/Super_SPC', data_dict, 'SPC_Wilenska_Zawor')
wrtie_to_excel(Valves_list, 'Valves')
