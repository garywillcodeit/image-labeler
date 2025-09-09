def get_format(mimetype):

    match mimetype:
        case "audio/aac":
            format = "aac"

        case "application/x-abiword":
            format = "abw"

        case "application/octet-stream":
            format = "arc"

        case "video/x-msvideo":
            format = "avi"

        case "application/vnd.amazon.ebook":
            format = "azw"

        case "application/octet-stream":
            format = "bin"

        case "image/bmp":
            format = "bmp"

        case "application/x-bzip":
            format = "bz"

        case "application/x-bzip2":
            format = "bz2"

        case "application/x-csh":
            format = "csh"

        case "text/css":
            format = "css"

        case "text/csv":
            format = "csv"

        case "application/msword":
            format = "doc"

        case "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            format = "docx"

        case "application/vnd.ms-fontobject":
            format = "eot"

        case "application/epub+zip":
            format = "epub"

        case "image/gif":
            format = "gif"

        case "text/html":
            format = "html"

        case "image/x-icon":
            format = "ico"

        case "text/calendar":
            format = "ics"

        case "application/java-archive":
            format = "jar"

        case "image/jpeg":
            format = "jpeg"

        case "image/jpg":
            format = "jpg"

        case "application/javascript":
            format = "js"

        case "application/json":
            format = "json"

        case "audio/midi":
            format = "midi"

        case "video/mpeg":
            format = "mpeg"

        case "application/vnd.apple.installer+xml":
            format = "mpkg"

        case "video/mp4":
            format = "mp4"

        case "application/vnd.oasis.opendocument.presentation":
            format = "odp"

        case "application/vnd.oasis.opendocument.spreadsheet":
            format = "ods"

        case "application/vnd.oasis.opendocument.text":
            format = "odt"

        case "audio/ogg":
            format = "oga"

        case "video/ogg":
            format = "ogv"

        case "application/ogg":
            format = "ogx"

        case "font/otf":
            format = "otf"

        case "image/png":
            format = "png"

        case "application/pdf":
            format = "pdf"

        case "application/vnd.ms-powerpoint":
            format = "ppt"

        case (
            "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        ):
            format = "pptx"

        case "application/x-rar-compressed":
            format = "rar"

        case "application/rtf":
            format = "rtf"

        case "application/x-sh":
            format = "sh"

        case "image/svg+xml":
            format = "svg"

        case "application/x-shockwave-flash":
            format = "swf"

        case "application/x-tar":
            format = "tar"

        case "image/tiff":
            format = "tiff"

        case "application/typescript":
            format = "ts"

        case "font/ttf":
            format = "ttf"

        case "application/vnd.visio":
            format = "vsd"

        case "audio/x-wav":
            format = "wav"

        case "audio/webm":
            format = "weba"

        case "video/webm":
            format = "webm"

        case "image/webp":
            format = "webp"

        case "font/woff":
            format = "woff"

        case "font/woff2":
            format = "woff2"

        case "application/xhtml+xml":
            format = "xhtml"

        case "application/vnd.ms-excel":
            format = "xls"

        case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            format = "xlsx"

        case "application/xml":
            format = "xml"

        case "application/vnd.mozilla.xul+xml":
            format = "xul"

        case "application/zip":
            format = "zip"

        case "video/3gpp":
            format = "3gp"

        case "audio/3gpp":
            format = "3gp"

        case "video/3gpp2":
            format = "3g2"

        case "audio/3gpp2":
            format = "3g2"

        case _:
            format = "7z"

    return format
