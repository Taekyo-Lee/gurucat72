Node.js v20.14.0
Running docker-entry.sh
/usr/src/app/redisinsight/api/node_modules/file-stream-rotator/lib/helper.js:16
            throw error;
            ^

Error: EACCES: permission denied, mkdir '/data/logs'
    at Object.mkdirSync (node:fs:1372:26)
    at makeDirectory (/usr/src/app/redisinsight/api/node_modules/file-stream-rotator/lib/helper.js:12:12)
    at FileStreamRotator.createNewLog (/usr/src/app/redisinsight/api/node_modules/file-stream-rotator/lib/FileStreamRotator.js:140:36)
    at FileStreamRotator.rotate (/usr/src/app/redisinsight/api/node_modules/file-stream-rotator/lib/FileStreamRotator.js:133:14)
    at new FileStreamRotator (/usr/src/app/redisinsight/api/node_modules/file-stream-rotator/lib/FileStreamRotator.js:22:14)
    at Object.getStream (/usr/src/app/redisinsight/api/node_modules/file-stream-rotator/lib/index.js:32:12)
    at new DailyRotateFile (/usr/src/app/redisinsight/api/node_modules/winston-daily-rotate-file/daily-rotate-file.js:80:57)
    at Object.<anonymous> (/usr/src/app/redisinsight/api/dist/config/logger.js:25:27)
    at Module._compile (node:internal/modules/cjs/loader:1358:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1416:10) {
  errno: -13,
  code: 'EACCES',
  syscall: 'mkdir',
  path: '/data/logs'
}
