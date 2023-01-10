class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sites = defaultdict(int)
        totalVisit = []

        for domain in cpdomains:
            count = domain.split()
            freq = int(count[0])
            sites[count[1]] += freq
            cp = count[1].split('.')
            length = len(cp)
            sites[cp[length-1]] += freq
            if length == 3:
                subdomain = cp[1]+"."+cp[2]
                sites[subdomain] += freq

        for key in sites.keys():
            totalVisit.append(str(sites[key]) + " " + key)

        return  totalVisit
