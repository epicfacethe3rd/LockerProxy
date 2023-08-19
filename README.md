# LockerProxy
Lockerproxy is a Fork of PluralKit designed to add much needed moderation features for server staff, most notably the ability for server staff to restrict who is allowed to proxy to a specific role

## Why?
Currently, PluralKit's dev team considers the ability for server staff to control who is allowed to proxy an unnacceptable addition to their bot, as they do not belive the greatly improved moderation abilities outweigh the possibility of syscourse based discrimination, as per [Issue 267](https://github.com/PluralKit/PluralKit/issues/267) and presumably many others on github

We disagree with this for a number of reasons.

While the point of view held by PluralKit's developement team is entirely valid, it is also worth noting it comes from a place where server staff are generally made up of a majority of systems, making it so server staff is generally all on the same page on how to handle incidents such as proxy misuse, lack of a system tag, and many other similar issues. Additionally, it's often that users are also majority systems, so users and server staff are *also* on the same page about what is and is not acceptable behavior and or proxy use. This is not the case on every server.

Many servers with PluralKit have a minority userbase of systems, and often times only one or two staff who are systems. Sometimes no staff at all who are systems. This can lead do a drastic disconnect in what is and what is not acceptable behavior in many servers, and cause much headache, heartache, and anger between staff and the minority userbase of systems. This should not be a suprise given the estimates of how much of the population are systems, and how even fewer may be publicly open about their disorder.

These conflicts between staff and systems can often result in systems becoming greatly displeased and upset with how staff handles system issues, and staff that feels a minorty userbase is constantly dragging them into conflicts they see as minor issues not worthy of "real" moderation. Often times, staff of such servers have stated they wished there was a way to restrict who can and cannot proxy, for a variety of reasons.

## Why not just Timeout/Mute/Kick/Ban problematic users instead as suggested?

The point of view that users who are trolling with proxies are problem users regardless of the fact they are proxying, is entirely valid. However, it is not at all uncommon for server staff to see such extremely dire issues, as instead complete non-issues not worthy of any kind of moderation, outside of occassionally chastizing the user doing so. We feel that the current PluralKit Development team is knowing or unknowingly ignoring this reality, albiet for the entirely understandable purpose of limiting syscourse and gatekeeping.

That said, it is not a stretch to say that many servers have outright abandoned PK, or ignored such moderation concerns from users outright as a result of PK's lack of moderation tools in this regard. We feel that while the intent to limit possible gatekeeping and syscourse is noble, it is in this case at odds with the primary purpose of an accessibility tool; to make it easier for disabled people to interact with abled people, but also as importantly, vice versa: to make it easier for abled people to interact with disabled people. We feel the inclusion of such moderation tools will make proxy tools more appealing to server staff, and thus increase the prevelance of them among majority singlet servers. In our opinion, this **Greatly** outweighs the possibility of gatekeeping and syscourse by bad actors, especially given that this likely will increase the presence and openness of systems in many communites, helping to normalize them

To quote an engineering instructor of mine: If your tool sucks to use, people aren't going to want to use it

Let's make proxy tools easier to use - for server staff as much as for systems

## How do i use LockerProxy?
Lockerproxy is currently in a form of closed beta while it is being developed. It's currently self hosted and maintained entirely by myself, out of pocket. If you want access to it, and you're a server operator, let me know, and we'll figure something out.

Fundamentally it's only about a hundred lines of code I personally have to maintain, but this is still very much a side project for myself. You're free to self host a version of it to try it out, I just ask that if I get to a more open and public release, you replace any self hosted instances of LockerProxy with the publicly hosted one, so that it's more accessible to other users.

As LockerProxy is a fork of Pluralkit, it *should* be able to be set up exactly the same as Pluralkit, albiet with a different command prefix \(`lp` instead of `pk` by default). Pluralkit's Readme is below.

# [PluralKit](https://github.com/PluralKit/PluralKit)
PluralKit is a Discord bot meant for plural communities. It has features like message proxying through webhooks, switch tracking, system and member profiles, and more.

**Do you just want to add PluralKit to your server? If so, you don't need any of this. Use the bot's invite link: https://discord.com/oauth2/authorize?client_id=466378653216014359&scope=bot%20applications.commands&permissions=536995904**

PluralKit has a Discord server for support, feedback, and discussion: https://discord.gg/PczBt78 

# Requirements
Running the bot requires [.NET 5](https://dotnet.microsoft.com/download), a PostgreSQL database and a Redis database. It should function on any system where the prerequisites are set up (including Windows).

Optionally, it can integrate with [Sentry](https://sentry.io/welcome/) for error reporting and [InfluxDB](https://www.influxdata.com/products/influxdb-overview/) for aggregate statistics.

# Configuration
Configuring the bot is done through a JSON configuration file. An example of the configuration format can be seen in [`pluralkit.conf.example`](https://github.com/PluralKit/PluralKit/blob/master/pluralkit.conf.example).
The configuration file needs to be placed in the bot's working directory (usually the repository root) and must be called `pluralkit.conf`.

The configuration file is in JSON format (albeit with a `.conf` extension). The following keys are available (using `.` to indicate a nested object level), bolded key names are required:
* **`PluralKit.Bot.Token`**: the Discord bot token to connect with
* **`PluralKit.Database`**: the URI of the database to connect to (in [ADO.NET Npgsql format](https://www.connectionstrings.com/npgsql/))
* **`PluralKit.RedisAddr`**: the `host:port` of a Redis database to connect to
* `PluralKit.Bot.Prefixes`: an array of command prefixes to use (default `["pk;", "pk!"]`).
* **`PluralKit.Bot.ClientId`**: the ID of the bot's user account, used for calculating the bot's own permissions and for the link in `pk;invite`.
* `PluralKit.SentryUrl` *(optional)*: the [Sentry](https://sentry.io/welcome/) client key/DSN to report runtime errors to. If absent, disables Sentry integration.
* `PluralKit.InfluxUrl` *(optional)*: the URL to an [InfluxDB](https://www.influxdata.com/products/influxdb-overview/) server to report aggregate statistics to. An example of these stats can be seen on [the public stats page](https://stats.pluralkit.me). 
* `PluralKit.InfluxDb` *(optional)*: the name of an InfluxDB database to report statistics to. If either this field or `PluralKit.InfluxUrl` are absent, InfluxDB reporting will be disabled.
* `PluralKit.LogDir` *(optional)*: the directory to save information and error logs to. If left blank, will default to `logs/` in the current working directory.

The bot can also take configuration from environment variables, which will override the values read from the file. Here, use `:` (colon) or `__` (double underscore) as a level separator (eg. `export PluralKit__Bot__Token=foobar123`) as per [ASP.NET config](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-3.1#environment-variables).

# Running

## Docker
The easiest way to get the bot running is with Docker. The repository contains a `docker-compose.yml` file ready to use.

* Clone this repository: `git clone https://github.com/PluralKit/PluralKit`
* Create a `pluralkit.conf` file in the same directory as `docker-compose.yml` containing at least `PluralKit.Bot.Token` and `PluralKit.Bot.ClientId` fields
  * (`PluralKit.Database` is overridden in `docker-compose.yml` to point to the Postgres container)
* Build the bot: `docker-compose build`
* Run the bot: `docker-compose up`

In other words:
```
$ git clone https://github.com/PluralKit/PluralKit
$ cd PluralKit
$ cp pluralkit.conf.example pluralkit.conf
$ nano pluralkit.conf  # (or vim, or whatever)
$ docker-compose up -d
```

## Manually
* Install the .NET 6 SDK (see https://dotnet.microsoft.com/download)
* Clone this repository: `git clone https://github.com/PluralKit/PluralKit`
* Create and fill in a `pluralkit.conf` file in the same directory as `docker-compose.yml`
* Run the bot: `dotnet run --project PluralKit.Bot`
  * Alternatively, `dotnet build -c Release -o build/`, then `dotnet build/PluralKit.Bot.dll`

(tip: use `scripts/run-test-db.sh` to run a temporary PostgreSQL database on your local system. Requires Docker.)

## Scheduled Tasks worker

There is a scheduled tasks worker that needs to be ran separately from the bot. This handles cleaning up the database, and updating statistics (system/member/etc counts, shown in the `pk;stats` embed).

Note: This worker is *not required*, and the bot will function correctly without it.

If you are running the bot via docker-compose, this is set up automatically.

If you run the bot manually you can run the worker as such:
* `dotnet run --project PluralKit.ScheduledTasks`
* or if you used `dotnet build` rather than `dotnet run` to run the bot: `dotnet build/PluralKit.ScheduledTasks.dll`

# Upgrading database from legacy version
If you have an instance of the Python version of the bot (from the `legacy` branch), you may need to take extra database migration steps.
For more information, see [LEGACYMIGRATE.md](./LEGACYMIGRATE.md).

# User documentation
See [the docs/ directory](./docs/README.md)

# License
This project is under the GNU Affero General Public License, Version 3. It is available at the following link: https://www.gnu.org/licenses/agpl-3.0.en.html
