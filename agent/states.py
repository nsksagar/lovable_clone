from pydantic import BaseModel, Field

class File(BaseModel):
    path : str = Field(
        description = "The path of the file to be created or modified"
    )
    purpose: str = Field(
        description = "The purpose of the file, e.g. 'Main application logic', 'data processing module' etc."
    )

#Schema is a class which you import from pydantic basemodel 
class Plan(BaseModel):  # Schema : <class '__main__.schema'>
    name : str = Field(description = 'The name of app to be built')

    description : str = Field(
        description = 'A one line description of the app to be built, e.g: "A web application for managing personal finances"'
    )
    techstack : str = Field(
        description = "The tech stack to be used for the App, e.g. 'python', 'react', 'javascript', 'flask' etc"
    )
    features : list[str] = Field(
        description = "A list of features that the app should have, e.g. 'user authentication', 'data visualization' etc"
    )
    files: list[File] = Field(
        description = "A list of files to be created, each each with a 'path' and 'purpose'"
    )
    
