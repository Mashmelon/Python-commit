import pandas as pd

class Analytics:

    @staticmethod
    def topper(records):
        """Return SID of highest overall score."""
        return max(records, key=lambda sid: sum(records[sid]["subjects"].values()))

    @staticmethod
    def subject_topper(records, subject):
        return max(records, key=lambda sid: records[sid]["subjects"][subject])

    @staticmethod
    def dataframe(records):
        """Convert to pandas DataFrame."""
        rows = []
        for sid, info in records.items():
            row = {"ID": sid, "Name": info["name"], **info["subjects"]}
            rows.append(row)
        return pd.DataFrame(rows)
