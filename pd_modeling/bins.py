import sys


bins = {
    "loan_amnt": [
        {
            "label": "(-inf, 2000)",
            "max": 2000
        },
        {
            "label": "(2000, 8000)",
            "max": 8000
        },
        {
            "label": "(8000, 12000)",
            "max": 12000
        },
        {
            "label": "(12000, 14400)",
            "max": 14400
        },
        {
            "label": "(14400, 20000)",
            "max": 20000
        },
        {
            "label": "(20000, 30000)",
            "max": 30000
        },
        {
            "label": "(30000, inf)",
            "max": sys.maxsize
        },
    ],
    "int_rate": [
        {
            "label": "(-inf, 9)",
            "max": 9
        },
        {
            "label": "(9, 11)",
            "max": 11
        },
        {
            "label": "(11, 13)",
            "max": 13
        },
        {
            "label": "(13, 15)",
            "max": 15
        },
        {
            "label": "(15, 17)",
            "max": 17
        },
        {
            "label": "(17, 23)",
            "max": 23
        },
        {
            "label": "(23, inf)",
            "max": sys.maxsize
        },
    ],
    "installment": [
        {
            "label": "(-inf, 100)",
            "max": 100
        },
        {
            "label": "(100, 250)",
            "max": 250
        },
        {
            "label": "(250, 380)",
            "max": 380
        },
        {
            "label": "(380, 430)",
            "max": 430
        },
        {
            "label": "(430, 570)",
            "max": 570
        },
        {
            "label": "(570, 1000)",
            "max": 1000
        },
        {
            "label": "(1000, inf)",
            "max": sys.maxsize
        },
    ],
    # "annual_inc": [
    #     {
    #         "label": "(-inf, 3.896000e+03)",
    #         "max": 3.896000e+03
    #     },
    #     {
    #         "label": "(3.896000e+03, 4.500000e+04)",
    #         "max": 4.500000e+04
    #     },
    #     {
    #         "label": "(4.500000e+04, 6.300000e+04)",
    #         "max": 6.300000e+04
    #     },
    #     {
    #         "label": "(6.300000e+04, 7.327738e+04)",
    #         "max": 7.327738e+04
    #     },
    #     {
    #         "label": "(7.327738e+04, 8.896000e+04)",
    #         "max": 8.896000e+04
    #     },
    #     {
    #         "label": "(8.896000e+04, 2.500000e+06)",
    #         "max": 2.500000e+06
    #     },
    #     {
    #         "label": "(2.500000e+06, inf)",
    #         "max": sys.maxsize
    #     },
    # ],
    "dti": [
        {
            "label": "(-inf, 14)",
            "max": 14
        },
        {
            "label": "(14, 16)",
            "max": 16
        },
        {
            "label": "(16, 18)",
            "max": 18
        },
        {
            "label": "(18, 23)",
            "max": 23
        },
        {
            "label": "(23, 30)",
            "max": 30
        },
        {
            "label": "(30, inf)",
            "max": sys.maxsize
        },
    ],
    "revol_bal": [
        {
            "label": "(-inf, 10.413000e+03)",
            "max": 10.413000e+03
        },
        {
            "label": "(10.413000e+03, 1.176400e+04)",
            "max": 1.176400e+04
        },
        {
            "label": "(1.176400e+04, 1.623020e+04)",
            "max": 1.623020e+04
        },
        {
            "label": "(1.623020e+04, 2.033300e+04	)",
            "max": 2.033300e+04
        },
        {
            "label": "(2.033300e+04	, 1.568995e+06)",
            "max": 1.568995e+06
        },
        {
            "label": "(1.568995e+06, inf)",
            "max": sys.maxsize
        },
    ],
    # "revol_util": [
    #     {
    #         "label": "(-inf, 42)",
    #         "max": 42
    #     },
    #     {
    #         "label": "(42, 48)",
    #         "max": 48
    #     },
    #     {
    #         "label": "(48, 56)",
    #         "max": 56
    #     },
    #     {
    #         "label": "(56, 75)",
    #         "max": 75
    #     },
    #     {
    #         "label": "(75, 600)",
    #         "max": 600
    #     },
    #     {
    #         "label": "(600, inf)",
    #         "max": sys.maxsize
    #     },
    # ],
    "total_acc": [
        {
            "label": "(-inf, 7)",
            "max": 7
        },
        {
            "label": "(7, 17)",
            "max": 17
        },
        {
            "label": "(17, 22)",
            "max": 22
        },
        {
            "label": "(22, 25)",
            "max": 25
        },
        {
            "label": "(25, 35)",
            "max": 35
        },
        {
            "label": "(35, 100)",
            "max": 100
        },
        {
            "label": "(100, inf)",
            "max": sys.maxsize
        },
    ],
    "total_pymnt": [
        {
            "label": "(-inf, 5500)",
            "max": 5500
        },
        {
            "label": "(5500, 9500)",
            "max": 9500
        },
        {
            "label": "(9500, 11000)",
            "max": 11000
        },
        {
            "label": "(11000, 15000)",
            "max": 15000
        },
        {
            "label": "(15000, 40000)",
            "max": 40000
        },
        {
            "label": "(40000, inf)",
            "max": sys.maxsize
        },
    ],
    "total_rec_prncp": [
        {
            "label": "(-inf, 3700)",
            "max": 3700
        },
        {
            "label": "(3700, 6800)",
            "max": 6800
        },
        {
            "label": "(6800, 8800)",
            "max": 8800
        },
        {
            "label": "(8800, 12000)",
            "max": 12000
        },
        {
            "label": "(12000, 25000)",
            "max": 25000
        },
        {
            "label": "(25000, inf)",
            "max": sys.maxsize
        },
    ],
    "total_rec_int": [
        {
            "label": "(-inf, 1200)",
            "max": 1200
        },
        {
            "label": "(1200, 1800)",
            "max": 1800
        },
        {
            "label": "(1800, 2500)",
            "max": 2500
        },
        {
            "label": "(2500, 3300)",
            "max": 3300
        },
        {
            "label": "(3300, 10000)",
            "max": 10000
        },
        {
            "label": "(10000, inf)",
            "max": sys.maxsize
        },
    ],
    "recoveries": [
        {
            "label": "(-inf, 200)",
            "max": 200
        },
        {
            "label": "(200, 600)",
            "max": 600
        },
        {
            "label": "(600, 10000)",
            "max": 10000
        },
        {
            "label": "(10000, 20000)",
            "max": 20000
        },
        {
            "label": "(20000, inf)",
            "max": sys.maxsize
        },
    ],
    "last_pymnt_amnt": [
        {
            "label": "(-inf, 400)",
            "max": 400
        },
        {
            "label": "(400, 550)",
            "max": 550
        },
        {
            "label": "(550, 2000)",
            "max": 2000
        },
        {
            "label": "(2000, 3200)",
            "max": 3200
        },
        {
            "label": "(3200, 10000)",
            "max": 10000
        },
        {
            "label": "(10000, inf)",
            "max": sys.maxsize
        },
    ]
}