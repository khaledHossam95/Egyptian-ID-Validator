from datetime import datetime, date

def validate_id(national_id):
    id_str = str(national_id) #Precaution if passed an integer value , would still work
    # Digit 1
    century = id_str[0]
    
    if century == "2":
        century_prefix = "19"
    elif century == "3":
        century_prefix = "20"
    else:
        return {"valid": False, "reason": "Invalid first digit (must be 2 or 3)"}

    # Digits 2-7 
    dob = id_str[1:7]
    full_dob = century_prefix + dob

    try:
        parsed_date = datetime.strptime(full_dob, "%Y%m%d").date()
    except ValueError:
        return {"valid": False, "reason": "Invalid date (digits 2-7)"}

    if parsed_date > date.today():
        return {"valid": False, "reason": "Date is in the future"}
    
    # Digits 8-9 
    province = id_str[7:9]
    province_dict = {
    "01": "Cairo",
    "02": "Alexandria",
    "03": "Port Said",
    "04": "Suez",
    "11": "Damietta",
    "12": "Dakahlia",
    "13": "Sharqia",
    "14": "Qalyubia",
    "15": "Kafr El Sheikh",
    "16": "Gharbia",
    "17": "Monufia",
    "18": "Beheira",
    "19": "Ismailia",
    "21": "Giza",
    "22": "Beni Suef",
    "23": "Fayoum",
    "24": "Minya",
    "25": "Assiut",
    "26": "Sohag",
    "27": "Qena",
    "28": "Aswan",
    "29": "Luxor",
    "31": "Red Sea",
    "32": "New Valley",
    "33": "Matrouh",
    "34": "North Sinai",
    "35": "South Sinai",
    "88": "Foreign"
    }
    try:
        parsed_province = province_dict[province]
    except KeyError:
        return {"valid": False, "reason": "Invalid province code (digits 8–9)"}
    
    # Digits 10-13
    parsed_births_same_day = int(id_str[10:12])
    gender = int(id_str[12])

    if gender % 2 != 0:
        parsed_gender = "Male"
    else :
        parsed_gender = "Female"

    
    return {"valid": True, 
            "birth_date": parsed_date,
            "province":parsed_province,
            "births_same_day":parsed_births_same_day,
            "gender":parsed_gender
            }