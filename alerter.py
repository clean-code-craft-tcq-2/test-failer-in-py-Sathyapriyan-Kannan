alert_failure_count = 0


def network_alert_stub(celcius, threshold=175):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius >= threshold:
        return 200
    else:
        return 500


def convert_fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius


def alert_in_celcius(fahrenheit, network_alert_key):
    celcius = convert_fahrenheit_to_celcius(fahrenheit)
    returnCode = network_alert_key(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1


alert_in_celcius(400.5, network_alert_stub)
alert_in_celcius(303.6, network_alert_stub)
assert (alert_failure_count == 1)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
