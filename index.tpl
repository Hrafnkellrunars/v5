<!DOCTYPE html>
    <html>

        <head>
            <title> Verkefni 5 </title>
            <meta charset="utf-8">
        </head>

        <header>
        </header>

        <body>
        % for i in data['results']:
            <h3>{{i['eventDateName']}}</h3>
            <h3>{{i['userGroupName']}}</h3>
            <h3>{{i['dateOfShow'][:10]}}</h3>
            <h3>{{i['dateOfShow'][11:][:5]}}</h3>
            <img src="{{i['imageSource']}}">
        % end
        </body>

    </html>