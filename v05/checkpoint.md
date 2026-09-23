## Routingtabell

```
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

     192.168.1.0/24 is variably subnetted, 8 subnets, 2 masks
C       192.168.1.0/26 is directly connected, GigabitEthernet0/0.10
L       192.168.1.1/32 is directly connected, GigabitEthernet0/0.10
C       192.168.1.64/26 is directly connected, GigabitEthernet0/0.20
L       192.168.1.65/32 is directly connected, GigabitEthernet0/0.20
C       192.168.1.128/26 is directly connected, GigabitEthernet0/0.30
L       192.168.1.129/32 is directly connected, GigabitEthernet0/0.30
C       192.168.1.192/26 is directly connected, GigabitEthernet0/0.99
L       192.168.1.193/32 is directly connected, GigabitEthernet0/0.99
```
## Min förklaring

- `192.168.1.0/24 is variably subnetted` betyder att adressområdet har delats upp i flera mindre nät med olika prefix.
- `C 192.168.1.0/26` är VLAN 10:s nät och är direkt anslutet via Gi0/0.10.
- `L 192.168.1.1/32` är routerns egen gatewayadress i VLAN 10.
- `C 192.168.1.64/26` är VLAN 20:s nät och är direkt anslutet via Gi0/0.20.
- `L 192.168.1.65/32` är routerns egen gatewayadress i VLAN 20.
- `C 192.168.1.128/26` är VLAN 30:s nät och är direkt anslutet via Gi0/0.30.
- `L 192.168.1.129/32` är routerns egen gatewayadress i VLAN 30.
- `C 192.168.1.192/26` är VLAN 99:s nät och är direkt anslutet via Gi0/0.99.
- `L 192.168.1.193/32` är routerns egen gatewayadress i VLAN 99.
- `Gateway of last resort is not set` betyder att routern ännu inte har någon default route mot internet.