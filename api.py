import requests


print("hello Poonam");


ruleHeaders = {'Authorization': 'Token token=y_NbAkKc66ryYTWUXYEu','Content-Type': 'application/json','Accept': 'application/vnd.pagerduty+json;version=2'}
response = requests.get("https://api.pagerduty.com/rulesets",headers=ruleHeaders);
print("rule sets list=======================",response.json());

ruleHeader = {'Authorization': 'Token token=u+Z-zxz1vs2CpUY9YD2g','Content-Type':'application/json','Accept': 'application/vnd.pagerduty+json;version=2'}
response1 = requests.get("https://api.pagerduty.com/rulesets/b84ca198-83e9-487e-b750-a403dbe3e6a9",headers=ruleHeader);
print("rule set b84ca198-83e9-487e-b750-a403dbe3e6a9============================",response1.json());


#response2 = requests.get("https://api.pagerduty.com/rulesets/b84ca198-83e9-487e-b750-a403dbe3e6a9/rules/f3f70d0c-e0c9-4135-b962-04c2b39900b1",headers=ruleHeader);
response2 = requests.get("https://api.pagerduty.com/rulesets/b84ca198-83e9-487e-b750-a403dbe3e6a9/rules/f3f70d0c-e0c9-4135-b962-04c2b39900b1",headers=ruleHeader);
print("rule with rule id======================================",response2.json());

data1={
  "rule": {
    "id": "202111003-ebab-4dd0-ba9d-fc28a41b7e7b",
    "position": 0,
    "disabled": False,
    "catch_all": False,
    "conditions": {
      "operator": "and",
      "subconditions": [
        {
          "operator": "matches",
          "parameters": {
            "value": "(?i)Poonam-test",
            "path": "headers.subject"
          }
        }
      ]
    },
    "time_frame": {
      "active_between": {
        "start_time": 1577880000000,
        "end_time": 1580558400000
      }
    },
    "actions": {
      "annotate": {
        "value": "This incident was created by a Poonam Event Rule.This is a test event rule from automation via api "
      },
      "route": {
        "value": "PI2KBWI"
      },
      "priority": {
        "value": "PCMUB6F"
      },
      "severity": {
        "value": "warning"
      },
      "extractions": [
        {
          "target": "dedup_key",
          "source": "details.error_summary",
          "regex": "Host (.*) is experiencing errors. This is a test event rule from automation via api"
        }
      ]
    }
  }
}

#ruleHeader1 = {'Authorization': 'Token token=u+Z-zxz1vs2CpUY9YD2g','Content-Type':'application/json','Accept': 'application/vnd.pagerduty+json;version=2'}
#print("Rule post ===================================")
#response3 = requests.post('https://api.pagerduty.com/rulesets/c85521b6-9600-4b84-9a5d-d27d30a983dc/rules',headers=ruleHeader1,data=data1)

#print("rule created====================",response3.json())

print("Rule put ===================================")
response4 = requests.post("https://api.pagerduty.com/rulesets/c85521b6-9600-4b84-9a5d-d27d30a983dc/rules",headers=ruleHeader,json=data1)
print("rule updated====================",response4.json())

