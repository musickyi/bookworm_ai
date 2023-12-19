from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
client = OpenAI()

class Book(BaseModel):
    bookId: int
    content: str

@app.post("/test")
def test(books: list[Book]):
    for book in books:  # Fix 1: Loop through books directly
        hi(book)

def hi(book: Book):  # Fix 2: Use 'book' instead of 'Book'
    print(book)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": book.content + " 이 문장이 유해한 단어를 포함한다면, 이 문장은 유해한 문장입니다를 말해주고 다른 이상한 말은 석지말고, 유해한 단어가 없다면 이 문장은 청결합니다라고 말해줘 다른 이상말은 석지말고"}
        ]
    )

    print(completion.choices[0].message)
