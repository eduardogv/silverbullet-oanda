import os
import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime, timedelta

# Note: for information on how to use this example code please read https://metaapi.cloud/docs/client/usingCodeExamples

token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI4YjFhZjQzMTU1OTdlMTI1YjczMWM1ODIxNzUxMjE4MiIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDQ4N2NhYTMtNGM3My00OGRjLTg3MDYtZTI1YzUxMzE1ZWUxIl19LHsiaWQiOiJtZXRhYXBpLXJlc3QtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNDg3Y2FhMy00YzczLTQ4ZGMtODcwNi1lMjVjNTEzMTVlZTEiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjA0ODdjYWEzLTRjNzMtNDhkYy04NzA2LWUyNWM1MTMxNWVlMSJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjA0ODdjYWEzLTRjNzMtNDhkYy04NzA2LWUyNWM1MTMxNWVlMSJdfSx7ImlkIjoibWV0YXN0YXRzLWFwaSIsIm1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNDg3Y2FhMy00YzczLTQ4ZGMtODcwNi1lMjVjNTEzMTVlZTEiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDQ4N2NhYTMtNGM3My00OGRjLTg3MDYtZTI1YzUxMzE1ZWUxIl19LHsiaWQiOiJtZXRhYXBpLXJlYWwtdGltZS1zdHJlYW1pbmctYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDQ4N2NhYTMtNGM3My00OGRjLTg3MDYtZTI1YzUxMzE1ZWUxIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNDg3Y2FhMy00YzczLTQ4ZGMtODcwNi1lMjVjNTEzMTVlZTEiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiOGIxYWY0MzE1NTk3ZTEyNWI3MzFjNTgyMTc1MTIxODIiLCJpYXQiOjE3MjAyNDAxNzgsImV4cCI6MTcyMjgzMjE3OH0.L3bdPG_eO_5ojQpPflIZVLyljCKVX60_hVT1KYEJNwK-v4GWTbyqueo-fGJMR8Yy-3QBdU_5HZU_yoE8Z4jdOJLA5RDD3_GYWljXsnUpL6pR6H7OLVyC9ME3zcGubViQjNC1ehr7m9BUFbn3kQNjI_DYEqUMIx2ZkE0vBBuoW0BvckG7EUXzqWxMkw_czsM7z7YENE5t9Y4tE77bP8r7TsM7t97to5UffAw2vmA4OkqxsqnukClkf6I7jtKIULFpghZfz80aYoSLZA5bW0NDKklAT6bJJeCV9Z0CGbE3-oDGqX8sFx2JoXW_qcCvW71lFWfI22ogIs3lT0pJgE4zqvZ7wrWM47_wjkRX7r5F1r8olDQJMVVGGRKjbnXFJ2nXhi20MLyVir4ho9ZPmSLSxT1lvQwftn0UfgxMsv4LOkBNb8TPm7waqme9uNuX24u29erNhzZxFTPJ6yKr0y-7Ku2Tr5iie9Ym6VS-i_2WDWL1THMldkBOTqSUrTGDy_7IslUzy-4OZq3oWkAIkMNGo0jtAMfqM9wNlvJ3tMvbYWiT959tJ_1nnk3bSqKoZmW66Nw789hz6HNuO8HfEbBKqotRShf601VIFwWI2P7VjxVy3rgpk-R2f4uu_W3e68boU61cR84iWhH0_RXwQAvnwrMpJEKa7wo1ggJGqWCpiCc'
accountId = os.getenv('ACCOUNT_ID') or '0487caa3-4c73-48dc-8706-e25c51315ee1'


async def test_meta_api_synchronization():
    api = MetaApi(token)
    try:
        account = await api.metatrader_account_api.get_account(accountId)
        initial_state = account.state
        deployed_states = ['DEPLOYING', 'DEPLOYED']

        if initial_state not in deployed_states:
            #  wait until account is deployed and connected to broker
            print('Deploying account')
            await account.deploy()

        print('Waiting for API server to connect to broker (may take couple of minutes)')
        await account.wait_connected()

        # connect to MetaApi API
        connection = account.get_rpc_connection()
        await connection.connect()

        # wait until terminal state synchronized to the local state
        print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
        await connection.wait_synchronized()

        # invoke RPC API (replace ticket numbers with actual ticket numbers which exist in your MT account)
        print('Testing MetaAPI RPC API')
        print('account information:', await connection.get_account_information())
        print('positions:', await connection.get_positions())
        # print(await connection.get_position('1234567'))
        print('open orders:', await connection.get_orders())
        # print(await connection.get_order('1234567'))
        print('history orders by ticket:', await connection.get_history_orders_by_ticket('1234567'))
        print('history orders by position:', await connection.get_history_orders_by_position('1234567'))
        print(
            'history orders (~last 3 months):',
            await connection.get_history_orders_by_time_range(
                datetime.utcnow() - timedelta(days=90), datetime.utcnow()
            ),
        )
        print('history deals by ticket:', await connection.get_deals_by_ticket('1234567'))
        print('history deals by position:', await connection.get_deals_by_position('1234567'))
        print(
            'history deals (~last 3 months):',
            await connection.get_deals_by_time_range(datetime.utcnow() - timedelta(days=90), datetime.utcnow()),
        )
        print('server time', await connection.get_server_time())

        # calculate margin required for trade
        print(
            'margin required for trade',
            await connection.calculate_margin(
                {'symbol': 'GBPUSD', 'type': 'ORDER_TYPE_BUY', 'volume': 0.1, 'openPrice': 1.1}
            ),
        )

        # trade
        print('Submitting pending order')
        try:
            result = await connection.create_limit_buy_order(
                'GBPUSD', 0.07, 1.0, 0.9, 2.0, {'comment': 'comm', 'clientId': 'TE_GBPUSD_7hyINWqAlE'}
            )
            print('Trade successful, result code is ' + result['stringCode'])
        except Exception as err:
            print('Trade failed with error:')
            print(api.format_error(err))
        if initial_state not in deployed_states:
            # undeploy account if it was undeployed
            print('Undeploying account')
            await connection.close()
            await account.undeploy()

    except Exception as err:
        print(api.format_error(err))
    exit()


asyncio.run(test_meta_api_synchronization())
