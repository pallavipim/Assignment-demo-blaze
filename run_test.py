import subprocess

file_1 = "feature/UserSignUp.feature"
file_2 = "feature/UserLogin.feature"
file_3 = "feature/Product_browsing.feature"
file_4 = "feature/Add_product_to_shopping_cart.feature"
file_5 = "feature/CheckOut.feature"
file_6 = "feature/LogOut.feature"

feature_files_order = [file_1, file_2, file_3, file_4, file_5, file_6]

behave_results = []

for feature_file in feature_files_order:
    result = subprocess.run(['behave', '-f', 'allure_behave.formatter:AllureFormatter', '-o', 'allure/results', feature_file], capture_output=True, text=True)
    behave_results.append(result)

allure_executable_path = "C:/Program Files/Allure/bin/allure.bat"  # Update this with the actual path

allure_generate_result = subprocess.run([allure_executable_path, 'generate', 'allure/results/', '-o', 'allure/reports', '--clean'], capture_output=True, text=True)

allure_open_result = subprocess.run([allure_executable_path, 'open', 'allure/reports'], capture_output=True, text=True)