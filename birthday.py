from datetime import date

DAYS_IN_SEASONS = [92, 94, 89, 90]


class Birthday:
    def __init__(self, birthday):
        self.birthday = birthday

    @staticmethod
    def _convert_date(c_date):
        month, day = map(int, c_date.split('-'))
        return date(1991, month, day)

    @property
    def dist(self):
        dist = (self._convert_date(self.birthday) -
                self._convert_date('03-20')).days
        return dist if dist >= 0 else 365 + dist

    @property
    def dist_deg(self):
        order = 0
        cumulative_days = DAYS_IN_SEASONS[order]
        angle_dist = 0
        while self.dist - cumulative_days > 0:
            angle_dist += 90
            order += 1
            cumulative_days += DAYS_IN_SEASONS[order]
        cumulative_days -= DAYS_IN_SEASONS[order]
        angle_dist += (self.dist - cumulative_days) * \
            90 / DAYS_IN_SEASONS[order]
        return angle_dist
