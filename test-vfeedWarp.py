from vfeedWarp import search_for_cve_by_cpe, search_for_cpe_by_cve
from vfeedWarp import search_for_cwe_by_cve,search_for_exploit_by_cve

exploit_id = search_for_exploit_by_cve('CVE-2014-2206')
print(exploit_id)

vuln_id = search_for_cve_by_cpe('cpe:/a:prosody:prosody:0.6.0')
print(vuln_id)

cpes = []
for cve in vuln_id:
    cpes.append(search_for_cpe_by_cve(cve))

print("printing first CPE")
print(cpes[0])
print(type(cpes))
print(cpes[1])






