package geasy

import (
	"strings"
)

func normalizeLocalName(localName string) string {
	cleanName := localName
	plusI := strings.Index(cleanName, "+")
	if plusI > 0 {
		cleanName = cleanName[0:plusI]
	}
	cleanName = strings.Replace(cleanName, ".", "", -1)
	return cleanName
}

func normalizeEmail(email string) string {
	atI := strings.Index(email, "@")
	localName := email[0:atI]
	domain := email[atI:]
	cleanName := normalizeLocalName(localName)
	return cleanName + domain
}

func numUniqueEmails(emails []string) int {
	uniEmails := make(map[string]bool, len(emails))
	for _, email := range emails {
		cleanEmail := normalizeEmail(email)
		uniEmails[cleanEmail] = true
	}
	return len(uniEmails)
}
