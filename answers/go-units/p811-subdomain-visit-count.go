package leetcode

import (
	"fmt"
	"strconv"
	"strings"
)

func subdomainVisits(cpdomains []string) []string {
	domainCountMap := make(map[string]int)
	for _, cpdomain := range cpdomains {
		parts := strings.SplitN(cpdomain, " ", 2)
		if len(parts) != 2 {
			fmt.Println(parts)
			continue
		}
		count, _ := strconv.Atoi(parts[0])
		domain := parts[1]
		domainCountMap[domain] = domainCountMap[domain] + count
		dotIndex1 := strings.IndexByte(domain, '.')
		dotIndex2 := strings.LastIndexByte(domain, '.')
		subdomain := domain[dotIndex1+1:]
		domainCountMap[subdomain] = domainCountMap[subdomain] + count
		if dotIndex2 != -1 && dotIndex1 != dotIndex2 {
			subdomain2 := domain[dotIndex2+1:]
			domainCountMap[subdomain2] = domainCountMap[subdomain2] + count
		}
	}
	result := []string{}
	for domain, count := range domainCountMap {
		record := strconv.Itoa(count) + " " + domain
		result = append(result, record)
	}
	return result
}
