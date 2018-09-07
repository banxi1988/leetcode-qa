package main

import (
	"fmt"
	"time"
)

type Term struct {
	Term      int
	beginTime string
}

func NormalizeStartDate(t time.Time) time.Time {
	wd := t.Weekday()
	if wd == time.Sunday {
		return t.AddDate(0, 0, 1)
	}
	decDays := wd - time.Monday
	return t.AddDate(0, 0, -int(decDays))
}

func CalcMondayOfWeek(firstMonday time.Time, week int) time.Time {
	return firstMonday.AddDate(0, 0, 7*(week-1))
}

func CalcDateInWeek(monday time.Time, weekday time.Weekday) time.Time {
	if weekday == time.Sunday {
		return monday.AddDate(0, 0, 6)
	}
	if weekday == time.Monday {
		return monday
	}
	incDays := int(weekday - time.Monday)
	return monday.AddDate(0, 0, incDays)
}

func main() {
	currentTerm := Term{20182, "2018-02-13"}
	startDate, _ := time.Parse("2006-01-02", currentTerm.beginTime)
	fmt.Println("startDate:", startDate)
	mondayOfFirstWeek := NormalizeStartDate(startDate)
	fmt.Println(" 第一周周1:", mondayOfFirstWeek)
	week18Monday := CalcMondayOfWeek(mondayOfFirstWeek, 18)
	fmt.Println(" 第18周，周1 :", week18Monday)
	week18Wed := CalcDateInWeek(week18Monday, time.Wednesday)
	fmt.Println(" 第18周，周3 :", week18Wed)

}
