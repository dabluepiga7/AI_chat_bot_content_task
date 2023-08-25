import whois
import requests
import json

# this fuction is getting the domain's expiration date and creation date if it exists, if not, it returns None for both Expiration adn Creation dates

def domains_info_whois(domain):
    try:
        who = whois.whois(domain)
        return who.creation_date, who.expiration_date
    except Exception as no:
        return None, None
    
# this fuction is getting the website's status code by using requests API 
def websites_status_code(domain):
    try:
        response = requests.get(f"http://{domain}")
        return response.status_code
    except requests.RequestException:
        return None
    
# this fuctions, is connectting to AbuseIPDB, but it also is getting whether this information is public or not, how many reports they have gotten and if the website is safe or not
def check_domain_abuse_report(domain):
    try:
        api = "INSERT_KEY_HERE"
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
    
# this is the main fuction so that all of the main commands could work without any issues.
    
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
    
    

    
    
