import os
import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime

# Note: for information on how to use this example code please read https://metaapi.cloud/docs/client/usingCodeExamples

token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI4YjFhZjQzMTU1OTdlMTI1YjczMWM1ODIxNzUxMjE4MiIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDQ4N2NhYTMtNGM3My00OGRjLTg3MDYtZTI1YzUxMzE1ZWUxIl19LHsiaWQiOiJtZXRhYXBpLXJlc3QtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNDg3Y2FhMy00YzczLTQ4ZGMtODcwNi1lMjVjNTEzMTVlZTEiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjA0ODdjYWEzLTRjNzMtNDhkYy04NzA2LWUyNWM1MTMxNWVlMSJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjA0ODdjYWEzLTRjNzMtNDhkYy04NzA2LWUyNWM1MTMxNWVlMSJdfSx7ImlkIjoibWV0YXN0YXRzLWFwaSIsIm1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNDg3Y2FhMy00YzczLTQ4ZGMtODcwNi1lMjVjNTEzMTVlZTEiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDQ4N2NhYTMtNGM3My00OGRjLTg3MDYtZTI1YzUxMzE1ZWUxIl19LHsiaWQiOiJtZXRhYXBpLXJlYWwtdGltZS1zdHJlYW1pbmctYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDQ4N2NhYTMtNGM3My00OGRjLTg3MDYtZTI1YzUxMzE1ZWUxIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNDg3Y2FhMy00YzczLTQ4ZGMtODcwNi1lMjVjNTEzMTVlZTEiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiOGIxYWY0MzE1NTk3ZTEyNWI3MzFjNTgyMTc1MTIxODIiLCJpYXQiOjE3MjAyNDAxODQsImV4cCI6MTcyMjgzMjE4NH0.D8hGtCFEsS3GCeoyBXssOdlnTerKTDt5FdGKrKIKpTU7Y8wSqh9N7wNyJH3lYZFF4Xq0y0jzzGl4OBlbdvuFS7Hn-94LIDIFF_69QDXIzqS7O-HLamF35ZzZ9MDW55zaLH_mnJK4iEDcr78Shao00VfAE-0Z7igqrBQnk5bwt5mKWeDMVd0gUonUnZKVEodooXG8xO9gMWOwUf61-K2NhgWnMQk0jHV0XRXABfrcyxQSuFOY3Hav3FoYYF4NMcphrG4-E8Yyusmhz4x46UQ8n1l8zlr65oTGfG2RZL7GObtDq7sGZ3uABA3Al1UMZgsei0DKopE4UlY1p8laruCrXGq7VsfXHhsRhwYXHLDw2Z5EGU6TTIi4HVJwkTgbyjKOrSJN887O-_uJtDMIZHnFhdsWhGGeCRPe6m0qFzy1K0T1fgH4McxVltIYcd108zXOZI7I-fuj1zcA10z3JUjSSvX8EEE1vePFEUHVDSNTnkoW40RTioilCjiPxLw3Lu28ovf1kikh5M4-D6fjQxPZP6-WmYSpjDsYy7ysI0lLhgwteCkVt9hu_43lbptpQIzOwUXdZMCMQGrdqIF6pRsqlqisUrE6ald_pYTuw8ooUxW9l1tNVL4b2KWA9qgQV4CN8O9SLXzmSu2lFL8zAyZ833iZlAyDN97k7CK1ONRqwCI'
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
        connection = account.get_streaming_connection()
        await connection.connect()

        # wait until terminal state synchronized to the local state
        print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
        await connection.wait_synchronized()

        # access local copy of terminal state
        print('Testing terminal state access')
        terminal_state = connection.terminal_state
        print('connected:', terminal_state.connected)
        print('connected to broker:', terminal_state.connected_to_broker)
        print('account information:', terminal_state.account_information)
        print('positions:', terminal_state.positions)
        print('orders:', terminal_state.orders)
        print('specifications:', terminal_state.specifications)
        print('EURUSD specification:', terminal_state.specification('EURUSD'))
        await connection.subscribe_to_market_data('EURUSD')
        print('EURUSD price:', terminal_state.price('EURUSD'))

        # access history storage
        history_storage = connection.history_storage
        print('deals:', history_storage.deals[-5:])
        print('deals with id=1:', history_storage.get_deals_by_ticket('1'))
        print('deals with positionId=1:', history_storage.get_deals_by_position('1'))
        print(
            'deals for the last day:',
            history_storage.get_deals_by_time_range(
                datetime.fromtimestamp(datetime.now().timestamp() - 24 * 60 * 60), datetime.now()
            ),
        )

        print('history orders:', history_storage.history_orders[-5:])
        print('history orders with id=1:', history_storage.get_history_orders_by_ticket('1'))
        print('history orders with positionId=1:', history_storage.get_history_orders_by_position('1'))
        print(
            'history orders for the last day:',
            history_storage.get_history_orders_by_time_range(
                datetime.fromtimestamp(datetime.now().timestamp() - 24 * 60 * 60), datetime.now()
            ),
        )

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
