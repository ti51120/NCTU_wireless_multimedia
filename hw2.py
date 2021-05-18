from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.util import dumpNodeConnections


def MininetTopo():
    net = Mininet()
    info("Create host nodes.\n")
    h1 = net.addHost("h1", mac='00:00:00:00:00:01', ip='10.0.0.1/8')
    h2 = net.addHost("h2", mac='00:00:00:00:00:02', ip='10.0.0.2/8')
    h3 = net.addHost("h3", mac='00:00:00:00:00:03', ip='10.0.0.3/8')
    h4 = net.addHost("h4", mac='00:00:00:00:00:04', ip='10.0.0.4/8')

    lis = [x for x in range(1, 6)]

    info("Create switch node.\n")
    # s1 = net.addSwitch("s1", failMode = 'standalone')
    for num in lis:
        name = "s" + str(lis[num - 1])
        MAC = '00:00:00:00:00:0' + str(lis[num - 1])
        net.addSwitch(name, mac=MAC, failMode='secure', protocols='OpenFlow13')

    info("Create Links.\n")
    net.addLink("s" + str(lis[0]), h1, bw=5)
    net.addLink("s" + str(lis[0]), h2, bw=5)
    net.addLink("s" + str(lis[4]), h3, bw=5)
    net.addLink("s" + str(lis[4]), h4, bw=5)
    net.addLink("s" + str(lis[0]), "s" + str(lis[1]), bw=5)
    net.addLink("s" + str(lis[1]), "s" + str(lis[4]), bw=5)
    net.addLink("s" + str(lis[0]), "s" + str(lis[2]), bw=5)
    net.addLink("s" + str(lis[2]), "s" + str(lis[3]), bw=5)
    net.addLink("s" + str(lis[3]), "s" + str(lis[4]), bw=5)

    info("Create controller to switch.\n")
    net.addController(controller=RemoteController, ip='192.168.1.152')

    info("Build and start network.\n")
    net.build()
    net.start()

    info("Dumping host connections.\n")
    dumpNodeConnections(net.hosts)

    info("Run the mininet CLI")
    CLI(net)


if __name__ == '__main__':
    setLogLevel('info')
    MininetTopo()