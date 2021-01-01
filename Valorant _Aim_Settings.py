from numpy import mean

print('Valorant Aim Sensitivity Settings according to DPI\n')
DPI_400 = [.415, .375, .674, .600, 1, .628, .8, .82, .67, .974, .6, .6, .44, .471, .514, .5, .53, .54, .88, .69, 1, .8, .653, .76, .629, .58, .6, .55, .53, .7, .82, .58, .913, .447, .55, .624, .471, .6, .59, .785, .55, .619, .79, .817, .43, .59, 1, .459, .630, .515, .6, .58, .52, .6, .4, 1.12, .942, .434, .691, .650, .809, .58, .7, .597, .425, .69, .48, .45, .758, .47, .628, .408, .62, .5, .45, .563, .55, .97, .6, .6, .55, .55, .5, .8, .585, .390, .82, .6, .57, .404, .628, .534, .85, .535, .512]
Average_Sensitivity_400 = str(float(mean(DPI_400)))
print('400 DPI:')
print(f'Collected {len(DPI_400)} different settings from pros...')
print(f'The average sensitivty for 400 DPI is: {Average_Sensitivity_400}')
print(f'The lowest number for 400 DPI is: {min(DPI_400)}')
print(f'The highest number for 400 DPI is: {max(DPI_400)}')


DPI_800 = [.485, .47, .485, .314, .235, .41, .215, .277, .4, .314, .283, .177, .177, .244, .3, .471, .3, .4, .314, .3, .37, .4, .44, .45, .4, .29, .41, .41, .314, .250, .380, .25, .31, .745, .5, .31, .485, .26, .33, .306, .27, .2, .245, .409, .409, .45, .345, .39 ,.49, .3, .4, .384, .4, .6 ,.24, .28 ,.3, .3, .3, .6, .3, .35, .65, .548, .5, .49, .3, .9, .311]
Average_Sensitivity_800 = str(float(mean(DPI_800)))
print('\n800 DPI:')
print(f'Collected {len(DPI_800)} different settings from pros...')
print(f'The average sensitivity for 800 DPI is: {Average_Sensitivity_800}')
print(f'The lowest number for 800 DPI is: {min(DPI_800)}')
print(f'The highest number for 800 DPI is: {max(DPI_800)}')