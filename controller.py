from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# Store MAC → port mapping
mac_to_port = {}

def _handle_ConnectionUp(event):
    log.info("Switch %s has connected", event.dpid)

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.dpid
    in_port = event.port

    if not packet.parsed:
        log.warning("Ignoring incomplete packet")
        return

    src = packet.src
    dst = packet.dst

    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    # Learn source MAC
    mac_to_port[dpid][src] = in_port

    # Check if destination known
    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]
    else:
        out_port = of.OFPP_FLOOD

    # Create flow rule
    msg = of.ofp_flow_mod()
    msg.match.in_port = in_port
    msg.actions.append(of.ofp_action_output(port=out_port))

    event.connection.send(msg)

    # Send packet
    pkt_out = of.ofp_packet_out()
    pkt_out.data = event.ofp
    pkt_out.actions.append(of.ofp_action_output(port=out_port))
    pkt_out.in_port = in_port

    event.connection.send(pkt_out)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Custom POX Controller Started")