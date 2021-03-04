import asyncio
import time


def async_main():
    async def say_after(delay, what):
        await asyncio.sleep(delay)
        # time.sleep(delay)
        print(f"{time.strftime('%X')} - {what}")

    async def main():
        print(f"{time.strftime('%X')} - start")
        c1 = say_after(1, 'hello')
        c2 = say_after(2, 'world')
        await asyncio.gather(c1, c2)
        print(f"{time.strftime('%X')} - finish")

    # 非同期IOのエントリポイント
    asyncio.run(main())


def sync_main():
    def say_after(delay, what):
        time.sleep(delay)
        print(what)

    def main():
        print(f"{time.strftime('%X')} - start")
        say_after(1, 'hello')
        say_after(2, 'world')
        print(f"{time.strftime('%X')} - finish")

    main()


async_main()
