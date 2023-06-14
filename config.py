import random

'''

     delay - delay between wallets
     mode  -  0 - your chains (need to fill chain and to) ; 1 - search nft in all chains and sending it if it founded in your choosen network

     avax   /   bsc   /   polygon

     chain - from chain
     to - to chain (or random mode - random.choice(['your chain','your chain']) 
     api - need moralis api https://admin.moralis.io/settings#secret-keys
'''

delay = (10, 600)
mode = 1
chain = 'bsc'          #   avax   /   bsc   /   polygon
to = 'avax'     # or random mode - random.choice(['your chain','your chain'])
api = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjA2NzE1OWQ5LWM5NzEtNDYxYi1iYjEzLWI1ODEzODA5ZGNlNSIsIm9yZ0lkIjoiMzQyMDc4IiwidXNlcklkIjoiMzUxNjYyIiwidHlwZUlkIjoiOGJjOWUxYzUtMGJmNS00NjA4LWI5ZDItZDRhNDU1MTliMjExIiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE2ODYxNTgwNjEsImV4cCI6NDg0MTkxODA2MX0.WJwrCuf_MLfqLOVtDqJwLsLRZU3J8EaG0nOEYQLgRr4'

info = {'avax':('https://snowtrace.io/tx/','https://rpc.ankr.com/avalanche'),
        'polygon':('https://polygonscan.com/tx/','https://polygon-rpc.com'),
        'bsc':('https://bscscan.com/tx/','https://bscrpc.com')}