import unittest

from medilink_contract import build_summary


class BuildSummaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.patient = {"patient_id": "P-1001", "name": "Alex Morgan"}
        self.appointments = [{"appointment_id": "A-2001"}]

    def test_summary_preserves_required_public_contract(self) -> None:
        summary = build_summary(self.patient, self.appointments)

        self.assertEqual(
            set(summary),
            {"patient", "appointments", "clinic_status"},
        )
        self.assertEqual(summary["patient"], self.patient)
        self.assertEqual(summary["appointments"], self.appointments)
        self.assertEqual(summary["clinic_status"], "ACTIVE")

    def test_summary_copies_top_level_containers(self) -> None:
        summary = build_summary(self.patient, self.appointments)

        self.assertIsNot(summary["patient"], self.patient)
        self.assertIsNot(summary["appointments"], self.appointments)

    def test_summary_normalizes_clinic_status(self) -> None:
        summary = build_summary(
            self.patient,
            self.appointments,
            " maintenance ",
        )

        self.assertEqual(summary["clinic_status"], "MAINTENANCE")

    def test_rejects_non_dictionary_patient(self) -> None:
        with self.assertRaisesRegex(ValueError, "patient must be a dictionary"):
            build_summary([], self.appointments)

    def test_rejects_missing_or_empty_patient_id(self) -> None:
        for patient in ({}, {"patient_id": "  "}):
            with self.subTest(patient=patient):
                with self.assertRaisesRegex(ValueError, "patient_id"):
                    build_summary(patient, self.appointments)

    def test_rejects_non_list_appointments(self) -> None:
        with self.assertRaisesRegex(ValueError, "appointments must be a list"):
            build_summary(self.patient, ())

    def test_rejects_empty_or_non_string_clinic_status(self) -> None:
        for status in ("  ", None):
            with self.subTest(status=status):
                with self.assertRaisesRegex(ValueError, "clinic_status"):
                    build_summary(self.patient, self.appointments, status)


if __name__ == "__main__":
    unittest.main()
