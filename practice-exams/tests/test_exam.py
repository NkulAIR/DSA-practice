import pytest
from io import StringIO
import sys
import assessment as app

class TestAssessment:
    # --- Q1 Taxi Fare ---
    def test_taxi_fare_basic(self):
        assert app.taxi_fare_calculator([1, 2, 1]) == 80 # 4 people * 20

    def test_taxi_fare_empty(self):
        assert app.taxi_fare_calculator([]) == 0

    def test_taxi_fare_large_group(self):
        assert app.taxi_fare_calculator([10, 5]) == 300

    # --- Q2 Academic Record ---
    def test_academic_mixed(self):
        assert app.academic_record([80, 50, 49]) == ["Distinction", "Pass", "Fail"]

    def test_academic_boundaries(self):
        assert app.academic_record([75, 74, 50, 49]) == ["Distinction", "Pass", "Pass", "Fail"]

    def test_academic_empty(self):
        assert app.academic_record([]) == []

    # --- Q3 USSD Menu ---
    def test_ussd_correct_first_try(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('1\n'))
        captured = StringIO()
        sys.stdout = captured
        app.ussd_menu('1')
        sys.stdout = sys.__stdout__
        assert "Bundle Purchased!" in captured.getvalue()

    def test_ussd_retry_logic(self, monkeypatch):
        # Enters '2', then '9', then '1' (correct)
        monkeypatch.setattr('sys.stdin', StringIO('2\n9\n1\n'))
        captured = StringIO()
        sys.stdout = captured
        app.ussd_menu('1')
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        assert output.count("Invalid selection") == 2
        assert "Bundle Purchased!" in output

    # --- Q4 Load Shedding ---
    def test_streak_normal(self):
        assert app.load_shedding_streak([1, 0, 1, 1, 1, 0]) == 3

    def test_streak_split(self):
        assert app.load_shedding_streak([1, 1, 0, 1, 1, 1, 1]) == 4

    def test_streak_none(self):
        assert app.load_shedding_streak([0, 0, 0]) == 0

    def test_streak_all(self):
        assert app.load_shedding_streak([1, 1, 1]) == 3

    # --- Q5 Pothole Detector ---
    def test_pothole_basic(self):
        # 20 is > 5 and > 5
        assert app.pothole_detector([5, 5, 20, 5, 5]) == [20]

    def test_pothole_multiple(self):
        assert app.pothole_detector([1, 5, 1, 6, 1]) == [5, 6]

    def test_pothole_flat(self):
        assert app.pothole_detector([5, 5, 5, 5]) == []

    def test_pothole_edges(self):
        # Edges cannot be potholes as they don't have two neighbors
        assert app.pothole_detector([10, 5, 5, 10]) == []

    # --- Q6 License Plate ---
    def test_plates_valid(self):
        res = app.license_plate_validator(["ABC 123 GP"])
        assert res['valid'] == ["ABC 123 GP"]
        assert res['invalid'] == []

    def test_plates_mixed(self):
        plates = ["ABC 123 GP", "XYZ 999 KZ", "BadPlate"]
        res = app.license_plate_validator(plates)
        assert "ABC 123 GP" in res['valid']
        assert "XYZ 999 KZ" in res['invalid'] # Doesn't end with GP
        assert "BadPlate" in res['invalid']

    def test_plates_format_check(self):
        # "123 ABC GP" is invalid order
        res = app.license_plate_validator(["123 ABC GP"])
        assert "123 ABC GP" in res['invalid']

    # --- Q7 Electricity ---
    def test_elec_survive(self):
        assert app.prepaid_electricity(100, [10, 10, 10]) == "Power remains. Units left: 70."

    def test_elec_cut(self):
        # 50 - 20 (30) - 20 (10) - 20 (-10) -> Day 3
        assert app.prepaid_electricity(50, [20, 20, 20]) == "Power cut on day 3."

    def test_elec_exact_zero(self):
        # Depending on logic, 0 might count as power remains or cut. 
        # Usually 0 means lights are off in prepaid logic, or just about to go off.
        # Let's assume 0 is technically "remains" but next usage kills it, 
        # OR usually < 0 is the cut. Let's stick to < 0 for cut.
        assert "Units left: 0" in app.prepaid_electricity(20, [20])