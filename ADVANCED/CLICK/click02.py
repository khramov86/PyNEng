import subprocess
import click


@click.command()
@click.argument("ip_address")
@click.option("--count", "-c", default='3', help='How many times to ping', type=click.IntRange(1,10))
def ping_ip(ip_address, count):
    """

    :param ip_address:
    :param count:
    :return:
    """
    reply = subprocess.run(
        f"ping -n {count} {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='cp1251',
    )
    if reply.returncode == 0:
        print(f'IP address {ip_address} is reachable')

    else:
        print(f'IP address {ip_address} is unreacheble')


if __name__ == "__main__":
    ping_ip()
