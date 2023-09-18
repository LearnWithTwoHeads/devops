const testButton = document.getElementById("test-button");
const namesDiv = document.getElementById("names");
const body = document.getElementById("names-body");

const preNames = ["Yoofi", "Paak", "Adjoa"];

testButton.addEventListener("click", addName);

async function addName() {
  const name = document.getElementById("text-name-input");

  if (name.value !== "") {
    const response = await fetch(`http://${IP_ADDRESS}:8080/names/${name.value}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
    });

    const nameToAdd = await response.json();
    const addedName = document.createElement("h3");
    addedName.innerText = nameToAdd["name"];
    namesDiv.appendChild(addedName);
  }
}

async function getNames() {
  try {
    const response = await fetch(`http://${IP_ADDRESS}:8080/names`);

    const allNames = await response.json();

    const names = allNames["names"];

    names.forEach((name) => {
      const nameElem = document.createElement("h3");
      nameElem.innerText = name;

      namesDiv.appendChild(nameElem);
    });
  } catch (err) {
    console.log("this is the error: ", err);
  }
}

body.onload = getNames();
