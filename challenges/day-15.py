"""
Heavy Rain Alert

Difficulty: Medium

You can see information about when some of the areas around Bangalore start to get flooded.
“KR Puram” - Risk of flood if it rains more than 4 cm.
“Bellandur” - Risk of flood if it rains more than 5 cm.
“Gangothri Road” - Risk of flood if it rains more than 10 cm.
Create an object which stores the present amount of rain and the above information about the 3 given areas with the threshold rain in cm. The object should have a method, which will print the following message - “Heavy rain in {area}. Risk of flood” if rain exceeds the threshold value for any region.
Given the rain amount in cm as input, instantiating an object and calling the method should print the appropriate messages.

Examples:

Test Case 1:
Input: 5
Output:
Heavy rain in KR Puram. Risk of flood
Explanation: Rain threshold value for KR Puram is 4. Given rain amount is greater than 4. So we print a message for KR Puram. It isn't greater than 5 or 10, so we don't print any message for the other areas.

Test Case 2:
Input: 12
Output:
Heavy rain in KR Puram. Risk of flood
Heavy rain in Bellandur. Risk of flood
Heavy rain in Gangothri Road. Risk of flood
Explanation:
12 is greater than all thresholds 4, 5 and 10. So we print 3 messages.
"""


class HeavyRainAlert:
    """Class to check for heavy rain alerts in Bangalore areas"""

    flood_risk_by_area = {
        'KR Puram': 4,
        'Bellandur': 5,
        'Gangothri Road': 10
    }

    def __init__(self, rain_amount: int):
        self.rain_amount = rain_amount

    def get_alerts(self) -> list[str]:
        """Checks for flood risk in each area and a list of alert messages"""
        def template_alert(area):
            return f"Heavy rain in {area}. Risk of flood."

        return [template_alert(area) for area,
                threshold in self.flood_risk_by_area.items() if self.rain_amount > threshold]


def test(rain_amount: int, expected_areas: list[int]):
    areas = ["KR Puram", "Bellandur", "Gangothri Road"]
    alerter = HeavyRainAlert(rain_amount)
    expected = [
        f"Heavy rain in {areas[i]}. Risk of flood." for i in expected_areas]

    assert alerter.get_alerts() == expected


def test_1():
    test(5, [0])


def test_2():
    test(12, [0, 1, 2])


def test_3():
    test(0, [])


def test_4():
    test(10, [0, 1])


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    print("All tests passed.")
