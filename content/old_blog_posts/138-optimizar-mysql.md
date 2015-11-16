+++
date = "2010-04-04"
title = "Optimizar MYSQL."
+++
Si tienes la necesidad de optimizar mysql puedes usar el siguiente programa: MySQLTunner http://blog.mysqltuner.com/download/ Lo descargas con

> wget mysqltuner.ply lo ejecutas> perl mysqltuner.plTe preguntara el usuario de la base de datos, y el password de la base de datos. y te dara instrucciones de que variables configurar en el archivo my.cnf asi como consejos para tus aplicaciones que usen mysql. Ejemplo> Server:~# perl mysqltuner.pl >> MySQLTuner 1.0.1 - Major Hayden <major>
> &gt;&gt; Bug reports, feature requests, and downloads at http://mysqltuner.com/
> &gt;&gt; Run with '--help' for additional options and output filtering
> Please enter your MySQL administrative login: root
> Please enter your MySQL administrative password: 
> 
> -------- General Statistics --------------------------------------------------
> [--] Skipped version check for MySQLTuner script
> [OK] Currently running supported MySQL version 5.0.51a-24+lenny3-log
> [OK] Operating on 64-bit architecture
> 
> -------- Storage Engine Statistics -------------------------------------------
> [--] Status: +Archive -BDB -Federated -InnoDB -ISAM -NDBCluster 
> [--] Data in MyISAM tables: 175M (Tables: 419)
> [OK] Total fragmented tables: 0
> 
> -------- Performance Metrics -------------------------------------------------
> [--] Up for: 20m 47s (6K q [5.370 qps], 1K conn, TX: 21M, RX: 525K)
> [--] Reads / Writes: 96% / 4%
> [--] Total buffers: 138.0M global + 2.6M per thread (300 max threads)
> [OK] Maximum possible memory usage: 925.5M (45% of installed RAM)
> [OK] Slow queries: 0% (0/6K)
> [OK] Highest usage of available connections: 1% (4/300)
> [OK] Key buffer size / total MyISAM indexes: 32.0M/31.8M
> [!!] Key buffer hit rate: 89.2% (14K cached / 1K reads)
> [OK] Query cache efficiency: 22.9% (839 cached / 3K selects)
> [OK] Query cache prunes per day: 0
> [OK] Sorts requiring temporary tables: 0% (0 temp sorts / 273 sorts)
> [!!] Joins performed without indexes: 13
> [OK] Temporary tables created on disk: 24% (96 on disk / 394 total)
> [OK] Thread cache hit rate: 99% (4 created / 1K connections)
> [!!] Table cache hit rate: 5% (47 open / 925 opened)
> [OK] Open file limit used: 2% (95/4K)
> [OK] Table locks acquired immediately: 100% (2K immediate / 2K locks)
> 
> -------- Recommendations -----------------------------------------------------
> General recommendations:
> MySQL started within last 24 hours - recommendations may be inaccurate
> Adjust your join queries to always utilize indexes
> Increase table_cache gradually to avoid file descriptor limits
> Variables to adjust:
> join_buffer_size (&gt; 128.0K, or always use indexes with joins)
> table_cache (&gt; 2048)</major>
