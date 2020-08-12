
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

from scionlab.models.core import Host
from scionlab.models.user_as import UserAS, AttachmentPoint



def useras_ap():
    print('Total user ASes: %d' % UserAS.objects.count())
    print('By attachment point:')
    aps = AttachmentPoint.objects.all()
    for ap in aps:
        c = UserAS.objects.filter(attachment_point=ap).count()
        print('%s : %d' % (ap ,c))


def create_one_date_per_month(fromdate, todate):
    ret = []
    lastdate = fromdate
    while True:
        d = lastdate + relativedelta(months=1)
        if d > todate:
            break
        ret.append(d)
        lastdate = d
    return ret


def user_ases_created_before(fromdate):
    aa = UserAS.objects.all()[0]
    c = UserAS.objects.filter(created_date__lt=fromdate).count()
    return c


def user_ases_modified_before(fromdate):
    aa = UserAS.objects.all()[0]
    c = UserAS.objects.filter(modified_date__lt=fromdate).count()
    return c


def user_ases_by_created():
    print('user ases by created')
    dates = create_one_date_per_month(datetime(2019, 1, 1, 0, 0, 0),datetime(2019, 12, 1, 0, 0, 0))
    for d in dates:
        c = user_ases_created_before(d)
        print(d, c)


def user_ases_by_modified():
    print('user ases by modified')
    dates = create_one_date_per_month(datetime(2019, 1, 1, 0, 0, 0),datetime(2019, 12, 1, 0, 0, 0))
    for d in dates:
        c = user_ases_modified_before(d)
        print(d, c)


def user_ases_active_inactive():
    userases = UserAS.objects.all()
    active = inactive = 0
    for uas in userases:
        # print(type(uas))
        try:
            if uas.is_active():
                active += 1
            else:
                inactive += 1
        except:
            inactive += 1
    print('user ases active, inactive = (%d, %d)' % (active,inactive))


def user_ases_vpn_nonvpn():
    userases = UserAS.objects.all()
    vpn = nonvpn = 0
    for uas in userases:
        if uas.is_use_vpn():
            vpn += 1
        else:
            nonvpn += 1
    print('user ases vpn, nonvpn = (%d, %d)' % (vpn, nonvpn))


def user_ases_by_install_type():
    types = ['VM', 'PKG', 'SRC']
    for t in types:
        c = UserAS.objects.filter(installation_type=t).count()
        print('%s : %d' % (t, c))


def run(*args):
    useras_ap()
    user_ases_by_created()
    user_ases_by_modified()
    user_ases_active_inactive()
    user_ases_vpn_nonvpn()
    user_ases_by_install_type()


# def main(argv):
#     return 0

# if __name__ == '__main__':
#     sys.exit(main(sys.argv))