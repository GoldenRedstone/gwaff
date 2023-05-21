import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

from plotter import Plotter


class Growth(Plotter):
    def sort(self):
        data = [self.read_row(row)[1] for index, row in self.data.iterrows()]
        self.data['Change'] = [row[-1] - row[0] for row in data]
        self.data.sort_values(by='Change', inplace=True, ascending=False)

    def read_row(self, row):
        xs = []
        values = []
        startval = None
        for i in self.dates:
            date = datetime.fromisoformat(i)
            if self.start_date and date < self.start_date:
                continue
            if row[i] is None or pd.isna(row[i]):
                continue

            startval = startval or row[i]
            if row['ID'] in [232123888073572354] and self.special:
                values.append(0 * (row[i] - startval))
            else:
                values.append(row[i] - startval)
            xs.append(date)
        if len(values) <= 1:
            return None, [0, 0]

        return xs, values

    def configure(self):
        super().configure()
        
        self.ax.set_ylabel("XP Growth")
        self.ax.set_ylim([0, self.maxxp * 1.05])


if __name__ == '__main__':
    data = pd.read_csv("gwaff.csv", index_col=0)

    plot = Growth(data, start_date=datetime.now() - timedelta(days=7))
    plot.draw(max_count=15)
    plot.annotate()
    plot.configure()

    plot.save()
    plot.show()
