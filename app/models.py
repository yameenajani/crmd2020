from django.db import models
from django.db.models.signals import post_save

SIDE = (
    ('Proposition', 'Proposition'),
    ('Opposition', 'Opposition')
)
# Create your models here.
class Debate(models.Model):
    dnum = models.PositiveIntegerField()
    team = models.CharField(max_length=5)
    side = models.CharField(max_length=15, choices=SIDE, default='Proposition')
    motion = models.CharField(max_length=200)
    link = models.CharField(max_length=100)

    def __str__(self):
        return "Debate " + str(self.dnum) + " - " + self.team + " - " + self.side

class Score(models.Model):
    dnum = models.PositiveIntegerField()
    prop = models.CharField(max_length=5)
    opp = models.CharField(max_length=5)
    props1p1j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Diction and vocal delivery - J1')
    props1p2j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Organization Of Points - J1')
    props1p3j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Quality Of Arguments - J1')
    props1p4j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Engagement with Opposite Team - J1')
    props1p5j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Analysis - J1')
    props1p6j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Coordination with partner - J1')
    props2p1j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Diction and vocal delivery - J1')
    props2p2j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Organization Of Points - J1')
    props2p3j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Quality Of Arguments - J1')
    props2p4j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Engagement with Opposite Team - J1')
    props2p5j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Analysis - J1')
    props2p6j1 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Coordination with partner - J1')
    opps1p1j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Diction and vocal delivery - J1')
    opps1p2j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Organization Of Points - J1')
    opps1p3j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Quality Of Arguments - J1')
    opps1p4j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Engagement with Opposite Team - J1')
    opps1p5j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Analysis - J1')
    opps1p6j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Coordination with partner - J1')
    opps2p1j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Diction and vocal delivery - J1')
    opps2p2j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Organization Of Points - J1')
    opps2p3j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Quality Of Arguments - J1')
    opps2p4j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Engagement with Opposite Team - J1')
    opps2p5j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Analysis - J1')
    opps2p6j1 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Coordination with partner - J1')
    props1p1j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Diction and vocal delivery - J2')
    props1p2j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Organization Of Points - J2')
    props1p3j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Quality Of Arguments - J2')
    props1p4j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Engagement with Opposite Team - J2')
    props1p5j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Analysis - J2')
    props1p6j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 1 - Coordination with partner - J2')
    props2p1j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Diction and vocal delivery - J2')
    props2p2j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Organization Of Points - J2')
    props2p3j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Quality Of Arguments - J2')
    props2p4j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Engagement with Opposite Team - J2')
    props2p5j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Analysis - J2')
    props2p6j2 = models.FloatField(default=0, verbose_name='Proposition Speaker 2 - Coordination with partner - J2')
    opps1p1j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Diction and vocal delivery - J2')
    opps1p2j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Organization Of Points - J2')
    opps1p3j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Quality Of Arguments - J2')
    opps1p4j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Engagement with Opposite Team - J2')
    opps1p5j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Analysis - J2')
    opps1p6j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 1 - Coordination with partner - J2')
    opps2p1j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Diction and vocal delivery - J2')
    opps2p2j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Organization Of Points - J2')
    opps2p3j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Quality Of Arguments - J2')
    opps2p4j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Engagement with Opposite Team - J2')
    opps2p5j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Analysis - J2')
    opps2p6j2 = models.FloatField(default=0, verbose_name='Opposition Speaker 2 - Coordination with partner - J2')

    def __str__(self):
        return "Scores of Debate - " + str(self.dnum)

class CalculatedScore(models.Model):
    dnum = models.PositiveIntegerField()
    prop = models.CharField(max_length=5)
    opp = models.CharField(max_length=5)
    pscore = models.FloatField()
    oscore = models.FloatField()

    def __str__(self):
        return "Final score of Debate - " + str(self.dnum)

def get_or_create_calculated_scores(sender, instance, created, **kwargs):
    if created:
        a = (float(instance.props1p1j1) * 0.1 +
        float(instance.props1p2j1) * 0.1 +
        float(instance.props1p3j1) * 0.3 +
        float(instance.props1p4j1) * 0.2 +
        float(instance.props1p5j1) * 0.2 +
        float(instance.props1p6j1) * 0.1)
        b = (float(instance.props1p1j2) * 0.1 +
        float(instance.props1p2j2) * 0.1 +
        float(instance.props1p3j2) * 0.3 +
        float(instance.props1p4j2) * 0.2 +
        float(instance.props1p5j2) * 0.2 +
        float(instance.props1p6j2) * 0.1)
        props1 = (a + b) / 2
        
        c = (float(instance.props2p1j1) * 0.1 +
        float(instance.props2p2j1) * 0.1 +
        float(instance.props2p3j1) * 0.3 +
        float(instance.props2p4j1) * 0.2 +
        float(instance.props2p5j1) * 0.2 +
        float(instance.props2p6j1) * 0.1)
        d = (float(instance.props2p1j2) * 0.1 +
        float(instance.props2p2j2) * 0.1 +
        float(instance.props2p3j2) * 0.3 +
        float(instance.props2p4j2) * 0.2 +
        float(instance.props2p5j2) * 0.2 +
        float(instance.props2p6j2) * 0.1)
        props2 = (c + d) / 2

        prop = (props1 + props2) / 2
        prop = "{:.3f}".format(prop)

        x = (float(instance.opps1p1j1) * 0.1 +
        float(instance.opps1p2j1) * 0.1 +
        float(instance.opps1p3j1) * 0.3 +
        float(instance.opps1p4j1) * 0.2 +
        float(instance.opps1p5j1) * 0.2 +
        float(instance.opps1p6j1) * 0.1)
        y = (float(instance.opps1p1j2) * 0.1 +
        float(instance.opps1p2j2) * 0.1 +
        float(instance.opps1p3j2) * 0.3 +
        float(instance.opps1p4j2) * 0.2 +
        float(instance.opps1p5j2) * 0.2 +
        float(instance.opps1p6j2) * 0.1)
        opps1 = (x + y) / 2

        z = (float(instance.opps2p1j1) * 0.1 +
        float(instance.opps2p2j1) * 0.1 +
        float(instance.opps2p3j1) * 0.3 +
        float(instance.opps2p4j1) * 0.2 +
        float(instance.opps2p5j1) * 0.2 +
        float(instance.opps2p6j1) * 0.1)
        w = (float(instance.opps2p1j2) * 0.1 +
        float(instance.opps2p2j2) * 0.1 +
        float(instance.opps2p3j2) * 0.3 +
        float(instance.opps2p4j2) * 0.2 +
        float(instance.opps2p5j2) * 0.2 +
        float(instance.opps2p6j2) * 0.1)
        opps2 = (z + w) / 2

        opp = (opps1 + opps2) / 2
        opp = "{:.3f}".format(opp)

        CalculatedScore.objects.get_or_create(dnum=instance.dnum, prop=instance.prop, opp=instance.opp, pscore=prop, oscore=opp)
        
post_save.connect(get_or_create_calculated_scores, sender=Score)