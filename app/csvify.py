from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse FileResponse, RedirectResponse
import uvicorn
import pandas as pd


app = Starlette(debug=True)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.route("/csvify")
class FileEndpoint(HTTPEndpoint):
    async def csvify(self, request):
        #Retrieve file, name and type from form request
        form = await request.form()
        contents = await form["upload_file"].read()
        file = form["upload_file"].file
        file_name = form["upload_file"].filename
        file_type = form["upload_file"].content_type
        csv_file_name = format(file_name.split('.')[0]) + ".csv"
        #Check if request has contents
        if not contents:
            return RedirectResponse("/?error=no_file")
        #Check if file type matches xslx
        if file_name != "" and file_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            pd.read_excel(file, 0, index_col=None).to_csv(csv_file_name, index=False)
            return FileResponse(csv_file_name, headers={"Content-Disposition": "attachment;filename={}".format(csv_file_name)})

        else:
            return RedirectResponse('/?error=invalid_file_type')


@app.route("/")
async def main(request):
    content = """
                <head>
                    <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
                </head>

                <body class="bg-grey-lighter h-screen font-sans">
                    <div class="container mx-auto h-full flex flex-col justify-center items-center">

                        <div class="w-1/3">
                            <h1 class="font-black text-6xl text-green-200 mb-6 text-center">CSVIFY</h1>
                        </div>
                        
                        <div class="border-teal p-8 border-t-12 bg-white mb-6 rounded-lg shadow-lg">
                            <form action="/csvify/" enctype="multipart/form-data" method="post">
                                <input  name="upload_file" type="file" multiple>
                                <input class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded" type="submit" value="CSVIFY">
                            </form>
                        </div>

                    </div>
                </body>
    """
    
    return HTMLResponse(content=content)


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=7070)