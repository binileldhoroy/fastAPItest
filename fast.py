from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel  
# from app1.models import Note
import requests
import json

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    url = "https://devapi.edelweissinsurance.com/oauth2/token"

    payload={}
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'x-api-key': 'pNmqGlRawQ4gT8hwzISIv2KENaVmGgif6q2uLe8A',
    'Authorization': 'Basic MzdhazBjOG9zYWVjZWFmbnUwZDRia2Q0cGo6MXI1aGJlZWY1Y2JrMmhiMGNpOWMwY2hkMDZsOWowc3Q2cHBiYmowYzh2ZXFjMnE2ZnA3Mw=='
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    access = json.loads(response.text)
    token = access['access_token']

    url = "https://devapi.edelweissinsurance.com/motor-two-wheeler/full-quote"

    payload = json.dumps({
    "source": "",
    "branch": "BANGALORE",
    "subIntermediaryCategory": "",
    "subIntermediaryCode": "",
    "subIntermediaryName": "",
    "subIntermediaryPhoneorEmail": "",
    "pospPanAadharNo": "",
    "businessSourceUniqueId": "",
    "accountNo": "",
    "agentName": "",
    "agentEmail": "shivakumar.bale@qualitykiosk.com",
    "float": "",
    "saleManagerCode": "26058",
    "saleManagerName": "Rahul B",
    "mainApplicantField": "1",
    "typeOfBusiness": "Rollover",
    "policyType": "Package Policy",
    "subPolicyType": "",
    "policyStartDate": "2022-10-15",
    "policyStartTime": "120100",
    "policyEndDay": "2023-10-14",
    "policyEndTime": "235900",
    "previousInsurancePolicy": "1",
    "policyHolderGender": "Male",
    "policyHolderOccupation": "Low to Medium",
    "kindOfPolicy": "Package With AddOn",
    "previousInsuranceCompanyName": "National Insurance Co. Ltd.",
    "previousInsuranceCompanyAddress": "Mumabi",
    "previousPolicyStartDate": "2021-10-15",
    "previousPolicyEndDate": "2022-10-14",
    "previousPolicyNo": "4545454",
    "natureOfLoss": "NA",
    "policyTenure": "1",
    "ownDamageStartDate": "",
    "ownDamageEndDate": "",
    "liabilityStartDate": "",
    "liablilityEndDate": "",
    "addOnStartDate": "",
    "addOnEndDate": "",
    "make": "HONDA",
    "model": "ACTIVA(2000-2015)",
    "variant": "DELUXE",
    "idvCity": "MUMBAI",
    "cubicCapacity": "110",
    "licencedCarryingCapacity": "2.0",
    "validLicenceNo": "Y",
    "fuelType": "Petrol",
    "newOrUsed": "Used",
    "yearOfManufacture": "2019",
    "registrationDate": "2019-10-14",
    "vehicalAge": "2",
    "engineNumber": "UNKNOWN0125",
    "chassisNumber": "UNKNOWN0123457",
    "fibreGlassFuelTank": "Y",
    "bodystyleDescription": "",
    "bodyType": "",
    "transmissionType": "",
    "validDrivingLicense": "",
    "handicapped": "N",
    "certifiedVintageCar": "N",
    "automobileAssociationMember": "Y",
    "antiTheftDeviceInstalled": "Y",
    "typeOfDeviceInstalled": "Burglary Alarm",
    "automobileAssociationMembershipNumber": "454545",
    "automobileAssociationMembershipExpiryDate": "2020-10-15",
    "stateCode": "10",
    "districtCode": "02",
    "vehicleSeriesNumber": "HD",
    "registrationNumber": "3535",
    "vehicleRegistrationNumber": "KA 02 HD 3535",
    "rtoLocationName": "KA-02",
    "rtoState": "KA",
    "rtoCityOrDistrict": "Banglore West",
    "clusterZone": "Cluster 1",
    "carZone": "A",
    "rtoZone": "10",
    "transferOfNCB": "Y",
    "transferOfNCBPercentage": "20",
    "proofDocumentDate": "2020-10-14",
    "proofProvidedForNCB": "NCB Reserving Letter",
    "applicableNCB": "20",
    "originalIDVValue": "106926",
    "requiredDiscountOrLoadingPercentage": "-40.0",
    "allowableDiscountOrLoading": "-40",
    "financeType": "",
    "financierName": "",
    "branchNameAndAddress": "",
    "salutation": "Mr.",
    "firstName": "Rajeev",
    "middleName": "",
    "lastName": "Radhakrishnan",
    "gender": "Male",
    "maritalStatus": "Single",
    "dateOfBirth": "1995-06-19",
    "nationality": "IN",
    "currentAddressLine1": "187/A",
    "currentAddressLine2": "Tent Road",
    "currentAddressLine3": "RM Nagara",
    "currentCountry": "IN",
    "pincode": "560016",
    "currentCity": "Bengaluru",
    "currentState": "13",
    "street": "Tent Road",
    "area": "RM Nagara",
    "location": "ShivajiNagar",
    "pan": "",
    "gstNo": "",
    "aadharNo": "",
    "mobileNumber": "8921892017",
    "emailId": "rajeev@autovert.in",
    "commissionContractID": "1000014234",
    "occupation": "Salaried",
    "nomineeName": "Radhakrishnan",
    "relationshipWithApplicant": "Father",
    "other": "",
    "isNomineeMinor": "N",
    "nomineeDOB": "1956-05-25",
    "nomineeAge": "64",
    "guardianName": "",
    "overrideAllowableDiscount": "Y",
    "inspectionNumber": "",
    "policyNumber": "",
    "renewalstatus": "New Policy",
    "annualmileageofthecar": "10000",
    "breakininsurance": "No Break",
    "typeofGrid": "GRID 1",
    "staffCode": "tetetyrte",
    "driverDetails": {
        "nameofDriver": "Rajeev",
        "dateofBirth": "1995-06-19",
        "genderofTheDriver": "Male",
        "ageOfDriver": "25",
        "relationshipwithProposer": "SELF",
        "driverExperienceinyears": "1",
        "middleName": "",
        "lastName": "Radhakrishnan"
    },
    "ContractDetails": [
        {
        "contract": "Own Damage Contract",
        "coverage": {
            "coverage": "Own Damage Coverage",
            "deductible": [
            "Own Damage Basis Deductible",
            "Voluntary Deductible"
            ],
            "subCoverage": [
            {
                "subCoverage": "Own Damage Basic",
                "limit": "Own Damage Basic Limit"
            }
            ]
        }
        },
        {
        "contract": "PA Compulsary Contract",
        "coverage": {
            "coverage": "PA Owner Driver Coverage",
            "subCoverage": {
            "subCoverage": "PA Owner Driver",
            "limit": "PA Owner Driver Limit",
            "sumInsured": "1500000"
            }
        }
        },
        {
        "contract": "Third Party Multiyear Contract",
        "coverage": {
            "coverage": "Legal Liability to Third Party Coverage",
            "deductible": "TP Deductible",
            "subCoverage": [
            {
                "subCoverage": "Third Party Basic Sub Coverage",
                "limit": "Third Party Property Damage Limit",
                "discount": "Third Party Property Damage Discount",
                "thirdPartyPropertyDamageLimit": "750000"
            },
            {
                "subCoverage": "PA Cover for unnamed Hirrer or Pillion Passenger",
                "limit": "PA Cover for unnamed Hirrer or Pillion Passenger Limit",
                "sumInsured": "10000",
                "noofPersons": "1"
            }
            ]
        }
        }
    ]
    })
    headers = {
    'x-api-key': 'Rn0Um8OBIv9kF17PIu4snf8BJBvSu597jOo1T7Lc',
    'Authorization': token,
    'Content-Type': 'application/json'
    }

    response1 = requests.request("POST", url, headers=headers, data=payload)

    print(response1.text)
    return {"responce": json.loads(response1.text)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}