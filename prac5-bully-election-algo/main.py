n = int(input('Enter number of nodes : '))
faulty = int(input(f'Enter faulty node (out of {1} to {n}) : '))
detector = int(input('Enter node that detected failure first : '))

def find_coordinator(detector, faulty, n):
    for node in range(detector, n+1):
        if node == faulty:
            continue
        print()
        print(f'---- Node {node} sending ELECTION message ----')
        oks = 0
        for neighbor in range(node+1,n+1):
            if neighbor != faulty:
                oks += 1
            print(f'ELECTION message sent to Node {neighbor}')

        if oks > 0:
            print(f'{oks} (OKs) received by Node {node}')
        else:
            print('Active higher priority process does NOT exist..')
            return node

def bully(detector, faulty, n):
    print(f'The Coordinator (Node {faulty}) has failed...')
    print(f'Node {detector} detected failure of coordinator...')
    print(f'Node {detector} initiating election process...')

    new_coordinator = find_coordinator(detector, faulty, n)

    print()
    print('----- RESULT OF ELECTION PROCESS-----')
    print(f'Node {new_coordinator} elected as new coordinator !!')
    print(f'Node {new_coordinator} sending message to inform that it is elected as new coordinator...')
    for neighbor in range(1, new_coordinator):
        print(f'message sent to Node {neighbor}')

bully(detector, faulty, n)
