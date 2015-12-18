import os


LIST_SAVE_PAGES_PYTHON_TEST = [
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/2/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/3/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/3/4/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/6/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/7/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/8/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/9/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/10/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/11/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/12/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/13/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/14/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/15/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/16/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/17/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/18/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/19/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/20/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test30.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test29.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test28.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test27.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test26.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test25.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test23.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test24.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test7.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test8.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test9.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test10.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test11.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test12.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test18.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test17.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test16.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test15.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test14.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test13.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test22.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test21.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test20.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test19.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test1.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test2.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test4.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test5.html',

]

LIST_SAVE_PAGES_PYTHON_TEST_HOME1 = [
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/2/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/3/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/3/4/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/6/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/7/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/8/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/9/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/10/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/11/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/12/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/13/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/14/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/15/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/16/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/17/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/18/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/19/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/20/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test1.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test2.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test4.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test5.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test7.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test8.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test9.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test10.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test11.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test12.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test13.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test14.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test15.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test16.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test17.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test18.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test19.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test20.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test21.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test22.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test23.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test24.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test25.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test26.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test27.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test28.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test29.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test30.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20TestFieled.html',

]

LIST_SAVE_PAGES_PYTHON_HOME = [
    "file:///home/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test1.html",
    "file:///home/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test.html"
]

LINK_TEST_PASS = [
    #'file:///home/nikolay/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/12/Upwork%20-%20Adaptive%20Skill%20Test.html',
    #'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/Upwork%20-%20Adaptive%20Skill%20Test.html',
    #"file:///home/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test_asci_fail.html"
    "file:///home/nikolay/Fortifier_proj/django_test/Upwork%20-%20Adaptive%20Skill%20Test4.html",
    "file:///home/nikolay/Fortifier_proj/django_test/Upwork%20-%20Adaptive%20Skill%20Test3.html",
    "file:///home/nikolay/Fortifier_proj/django_test/Upwork%20-%20Adaptive%20Skill%20Test1.html",
    "file:///home/nikolay/Fortifier_proj/django_test/Upwork%20-%20Adaptive%20Skill%20Test.html"
]

LINK_CSS_TEST = [
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test1.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test2.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test3.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test4.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test5.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test6.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test7.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test8.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test9.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test10.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test11.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test12.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test13.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test14.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test15.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test16.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test17.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test18.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test19.html',
    'file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/Upwork%20-%20Adaptive%20Skill%20Test20.html',
]


MAC_ADDRESS = ['54:04:a6:e2:db:a2', '08:00:27:02:33:ef', ]
#MAC_ADDRESS = []

PROXY_LIST = {
    "Germany": ["213.239.201.48", 60088],
    "China": ["218.200.66.196", 8080],
    "China": ["221.7.129.100", 1080],
    "China": ["101.6.52.217", 1080],
    "Canada": ["198.169.246.30", 80],
    "Ghana": ["197.159.142.97", 8080],
    "Russia": ["193.107.152.66", 3128],
    "Belarus": ["80.249.92.47", 8080],
    "Serbia": ["176.106.120.82", 8080],
    "Netherlands": ["84.106.211.32", 80],
    "Finland": ["188.165.141.151", 80],
    "Taiwan": ["114.38.156.130", 8088],
    "Germany": ["104.236.227.136", 9450],
    "USA": ["104.46.60.254", 8080],
    "USA": ["52.32.80.190", 80],
}

REG_EMAIL = '^[a-zA-Z0-9.-_]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}'
REG_LOGIN = '[a-zA-Z0-9._-]{2,}'
REG_PASSORD = '[A-Za-z0-9@#$%^&+=]{8,}'
REG_TEST_NAME = '[A-Za-z0-9+.# ]{2,}'

BASE_DIR = os.path.join(os.getcwd(), 'Robot')
