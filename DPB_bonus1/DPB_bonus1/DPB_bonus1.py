import redis

k='"scoreboard"'

if __name__ == '__main__':
    r=redis.Redis(host='localhost', port=6379, db=0)
    r.zadd(k, {"Alfred": 888})
    #10 dalsich hracu
    r.zadd(k, {"hrac1": 1})
    r.zadd(k, {"hrac2": 56})
    r.zadd(k, {"hrac3": 889})
    r.zadd(k, {"hrac4": 950})
    r.zadd(k, {"hrac5": 515})
    r.zadd(k, {"hrac6": 333})
    r.zadd(k, {"hrac7": 902})
    r.zadd(k, {"hrac8": 621})
    r.zadd(k, {"hrac9": 78})
    r.zadd(k, {"hrac10": 856})
    #vypis 3 nejlepsich hracu
    print(r.zrevrange(k, 0, 2, True))
    #vypis nejhorsiho hrace
    print(r.zrangebyscore(k, 0, 999, 0, 1))
    #pocet hracu pod 100 skore
    print(r.zcount(k,0,100))
    #hraci se skore vetsim jak 850
    print(r.zrevrangebyscore(k, 999, 850))
    #Alfredova pozice, zvysena o 1, protoze 1. misto ma pozici 0
    print(r.zrevrank(k, "Alfred")+1)
    #zvyseni Alfredova skore a jeho nova pozice
    r.zincrby(k, 12, "Alfred")
    print(r.zrevrank(k, "Alfred")+1)