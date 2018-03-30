from splinter import Browser

''' 
Made By Jacob Folsom 

Fill in the information below before running
'''

Studentid = 'Your Info'
name = 'Your Info'
middle = 'Your Info'
last = 'Your Info'
address = 'Your Info'
city = 'Your Info'
state = 'Your Info'
homezip = 'Your Info'
localaddress = 'Your Info'
cellphone = 'Your Info'
email = 'Your Info'
driversLicenseNum = 'Your Info'
vehicleType = 'Your Info' #This must be in all caps
VehicleModel = 'Your Info'
carYear = 'Your Info'
VehicleColor = 'Your Info' #Must be a common color and in all caps
VehicleLicensePlateNumber = 'Your Info'
LicenseState = 'Your Info'
VehicleOwner = 'Your Info' #This is your name in all caps
Insurance_Co_Name = 'Your Info'
Insurance_PolicyNum = 'Your Info'
Policy_Exp_Date = 'Your Info' #Must be in this format mmddyyyy

browser = Browser('chrome')
url = "https://cesi.reportexecdirect.com/Norwich/CESIReportExec/opr/OPRMain.aspx?IsAuth=1&groupid=102&groupname=PUBLIC+SAFETY"
browser.visit(url)
# Find and click the 'search' button
# Interact with elements


browser.find_by_id('ddPermitType').first
browser.find_option_by_text('STUDENT PARKING PERMIT').first.click()
browser.find_by_id('ddpermitPeriod').first
browser.find_option_by_text('ANNUAL').first.click()
browser.find_by_id('ddpermitRegistrationType').first
browser.find_option_by_text('RESIDENT STUDENT').first.click()
browser.find_by_id('btnContinue').first.click()
#2nd page
browser.find_by_id('Page_2_Id').first.fill(Studentid)
browser.find_by_id('Page_2_FirstName').first.fill(name)
browser.find_by_id('Page_2_MiddleName').first.fill(middle)
browser.find_by_id('Page_2_LastName').first.fill(last)
browser.find_by_id('ddType').first
browser.find_option_by_text('CONTACT').first.click()
browser.find_by_id('Page_2_HomeAddress').first.fill(address)
browser.find_by_id('Page_2_HomeCity').first.fill(city)
browser.find_by_id('Page_2_HomeState').first.fill(state)
browser.find_by_id('Page_2_HomeZip').first.fill(homezip)
browser.find_by_id('Page_2_LocalAddress').first.fill(localaddress)
browser.find_by_id('Page_2_Cell_Phone').first.fill(cellphone)
browser.find_by_id('Page_2_Work_Phone').first.fill(cellphone)
browser.find_by_id('Page_2_Email').first.fill(email)
browser.find_by_id('Page_2_Drivers_License').first.fill(driversLicenseNum)
browser.find_by_id('btnAdd').first.click()
browser.find_by_id('btnContinue').first.click()
#3rd page
browser.find_by_id('Page_3_VehicleType').first
browser.find_option_by_text(vehicleType).first.click()
browser.find_by_id('Page_3_VehicleModel').first.fill(VehicleModel)
browser.find_by_id('Page_3_Year').first.fill(carYear)
browser.find_by_id('Page_3_VehicleColor').first
browser.find_option_by_text(VehicleColor).first.click()
browser.find_by_id('Page_3_VehicleLicensePlateType').first
browser.find_option_by_text('AUTOMOBILE').first.click()
browser.find_by_id('Page_3_VehicleLicensePlateNumber').first.fill(VehicleLicensePlateNumber)
browser.find_by_id('Page_3_LicenseState').first.fill(LicenseState)
browser.find_by_id('Page_3_ddOwner').first
browser.find_option_by_text(VehicleOwner).first.click()
browser.find_by_id('Page_3_Insurance_Co_Name').first.fill(Insurance_Co_Name)
browser.find_by_id('Page_3_Insurance_Policy').first.fill(Insurance_PolicyNum)
browser.find_by_id('Page_3_Insurance_Policy_Exp_Date_textbox1').first.fill(Policy_Exp_Date)
browser.find_by_id('btnVehicleAdd').first.click()
browser.find_by_id('btnContinue').first.click()

if browser.find_by_id('Page_4_GeneralInfo_tr'):
    print('Done')
else:
    print('ISSUE')
