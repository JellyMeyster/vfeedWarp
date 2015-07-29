from vfeedModel import nvd_db, cve_cpe, cve_cwe, map_cve_exploitdb

# Take user input here and search
def processInput(userinput):
    user_inp = userinput
        
    
# Takes cpe and gives CVEs - Product to Vulnerability 
def search_for_cve_by_cpe(cpe):
    # Call data cleanse
    cves = []
        
    for x in cve_cpe.select().join(nvd_db)   .where(cve_cpe.cpeid == cpe):
        cves.append(x.cveid_id)
    return cves
            

# Takes CVE and gives CPEs - Vulnerability tied to multiple products
def search_for_cpe_by_cve(cve):
    cpes = []
    cves = cve
    
    for x in cve_cpe.select(cve_cpe.cpeid).join(nvd_db).where(nvd_db.cveid == cve):
        cpes.append(x.cpeid)
    return cpes



# Takes in CVEs and gives CWEs associated with CVEs 
def search_for_cwe_by_cve(cve):
    cves = []
    cwes = []

    for x in cve_cwe.select(cve_cwe.cweid).join(nvd_db).where(nvd_db.cveid ==cve):
        cwes.append(x.cweid)
    return(cwes)


        
# Takes CVEs and gives Exploit DB ID associated with the CVEs
def search_for_exploit_by_cve(cve):
    cves = []
    expid = []
    
    for x in map_cve_exploitdb.select(map_cve_exploitdb.exploitdbid).join(nvd_db).where(nvd_db.cveid == cve):
        expid.append(x.exploitdbid)
    return expid
        

if __name__ =='__main__':
    processInput(userInput)







