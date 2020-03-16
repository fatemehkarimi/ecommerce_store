from django.db.models import Avg
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64

from .models import Review

class RateAnalyze:
    def __init__(self, product):
        self.product = product

    def get_avg_rating(self):
        result = Review.objects.filter(
            product=self.product,
            rate__range=[1, 5]).aggregate(Avg('rate'))['rate__avg']
        
        if result is None:
            result = 0
        return round(result, 2)

    def get_rate_details(self):
        rate_detail = []
        count = 0
        for i in range(5, 0, -1):
            rate_detail.append(Review.objects.filter(
                product=self.product, rate=i).count())
            count += rate_detail[-1]
        
        if count == 0:
            return rate_detail
            
        for i in range(len(rate_detail)):
            rate_detail[i] = (rate_detail[i] * 100) / count
        return rate_detail

    def get_rate_plot(self):
        rate_detail = self.get_rate_details()
        rate_colors = ['#407a3a', '#4e9647', '#f5eb5b', '#f0a30a', '#eb2b09']

        np.random.seed(19680801)
        plt.rcdefaults()
        fig, ax = plt.subplots()

        stars = ('5 star', '4 star', '3 star', '2 star', '1 star')
        y_pos = np.arange(len(stars))
        error = 0

        ax.barh(y_pos, rate_detail, xerr=error, align='center', color=rate_colors)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(stars)
        ax.invert_yaxis()  # labels read top-to-bottom

        fig = plt.gcf()

        buff = io.BytesIO()
        fig.savefig(buff, format='png')
        buff.seek(0)
        string = base64.b64encode(buff.read())
        uri = urllib.parse.quote(string)
        return uri