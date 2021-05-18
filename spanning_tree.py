from mininet.cli import CLI
from mininet.link import Link
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm
from mininet.log import setLogLevel, info
from optparse import OptionParser
import random


def SetParse():
    parser = OptionParser()
    parser.add_option("-n", "--number", type="int", dest="switch_num", help="write 		the switch number",
                      default=3)
    return parser.parse_args()


def MininetTopo(switch_num):
    net = Mininet()

    info("Create host nodes.\n")

    h1 = net.addHost('h1', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', mac='00:00:00:00:00:02')
    # h3 = net.addHost('h3')

    info("Create switch nodes.\n")
    for sw in range(1, switch_num + 1):
        name = "s" + str(sw)
        net.addSwitch(name, failMode='secure', protocols='OpenFlow13')

    # s1 = net.addSwitch('s1')
    # s2 = net.addSwitch('s2')
    # s3 = net.addSwitch('s3')

    info("Create Links.\n")
    lis = []
    for num in range(1, switch_num + 1):
        lis.append(num)
    random.shuffle(lis)
    net.addLink("s" + str(lis[0]), h1)
    net.addLink("s" + str(lis[1]), h2)

    for node in range(1, switch_num + 1):
        for target in range(node + 1, switch_num + 1):
            net.addLink("s" + str(node), "s" + str(target))

    info("Create controller to switch.\n")
    net.addController(controller=RemoteController, ip='192.168.1.152')

    info("Build and start network.\n")
    net.build()
    net.start()

    info("Run mininet CLI.\n")
    CLI(net)


if '__main__' == __name__:
    setLogLevel('info')

    # Set Parse
    (options, args) = SetParse()
    print(options.switch_num)
    MininetTopo(options.switch_num)






