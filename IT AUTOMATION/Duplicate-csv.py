import pandas as pd
import sys
xl_file = r"C:\Users\rnsri\KT_BEAT_TEST\Request_KA_Monthly_June22.xlsx"
#final_path = r"C:\Users\rnsri\KT_BEAT_TEST"
xl_read = pd.read_excel(xl_file)
xl_read.drop_duplicates(subset = "Request ID")
xl_read.to_excel(r"C:\Users\rnsri\KT_BEAT_TEST\Request_KA_Monthly_June22_new.xlsx",index = False)
