import whois
import requests
import json

def domains_info_whois(domain):
    try:
        who = whois.whois(domain)
        return who.creation_date, who.expiration_date
    except Exception as no:
        return None, None
    
def websites_status_code(domain):
    try:
        response = requests.get(f"http://{domain}")
        return response.status_code
    except requests.RequestException:
        return None
    
def check_domain_abuse_report(domain):
    try:
        api = "9d7b7f27a89dd85fe444e0cb67984eeec3811c14fc11d9cf127d3bd73996bb5d2b56930e6877dfc2"
        report = requests.get(f"https://api.abuseipdb.com/api/v2/check?domain={domain}",
                              headers={"Key": api})
        data = report.json()
        abuse_history_public = data['data']['isPublic']
        if data['data']['totalReports'] > 50:
            report_count = data['data']['totalReports']
            abuse_history_public = data['data']['isPublic']
            
            
            return report_count, abuse_history_public, "Not safe"
        else:
            report_count = data['data']['totalReports']
            abuse_history_public = data['data']['isPublic']
            
            return report_count, abuse_history_public, "Safe"
    except Exception as no:
        return None, False, None
    
def main():
    domain = input("Enter the domain URL: ")
    
    creation_date, expiration_date = domains_info_whois(domain)
    
    if creation_date and expiration_date:
        print(f"Creation date: {creation_date}")
        print(f"Expiration date: {expiration_date}")
    else:
        print("domain is available ;) ")
        
    website_code = websites_status_code(domain)
    
    if website_code:
        print(f"Website status code: {website_code}")
    else:
        print("no info :( ")
        
    report_count, is_public, is_safe = check_domain_abuse_report(domain)
    if is_public == True:
        print(f"Abuse Report History: {is_public}")
        print(f"Abuse report total reports: {report_count}")
        print(f"Abuse report status: {is_safe}")
    else:
        print("no info :( ")
        
if __name__ == "__main__":
    main()
    
    
    
