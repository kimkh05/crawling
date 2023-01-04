import { useState } from "react";
import * as S from "./styles";

const Main = () => {
  const [file, setFile] = useState();
  const [array, setArray] = useState([]);
  const [name, setName] = useState("");
  const fileReader = new FileReader();

  const handleOnChange = (e) => {
    setFile(e.target.files[0]);
    setName(e.target.value);
  };

  const csvFileToArray = (string) => {
    const csvHeader = string.slice(0, string.indexOf("\n")).split(",");
    const csvRows = string.slice(string.indexOf("\n") + 1).split("\n");

    const array = csvRows.map((i) => {
      const values = i.split(",");
      const obj = csvHeader.reduce((object, header, index) => {
        object[header] = values[index];
        return object;
      }, {});
      return obj;
    });
    setArray(array);
  };

  const handleOnSubmit = (e) => {
    e.preventDefault();
    if (file) {
      fileReader.onload = (event) => {
        const text = event.target.result;
        csvFileToArray(text);
      };
      fileReader.readAsText(file);
    }
  };

  const headerKeys = Object.keys(Object.assign({}, ...array));

  return (
    <S.Wrapper>
      <S.WebTitle>How Many Of Developers</S.WebTitle>
      <S.UnderLine />
      <form>
        <S.InputCsvFiles
          type={"file"}
          id={"csvFileInput"}
          accept={".csv"}
          onChange={handleOnChange}
        />
        {name}
        <button
          onClick={(e) => {
            handleOnSubmit(e);
          }}
        >
          IMPORT CSV
        </button>
      </form>
      <br />
      <table>
        <thead>
          <tr key={"header"}>
            {headerKeys.map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {array.map((item) => (
            <tr key={item.id}>
              {Object.values(item).map((val) => (
                <td style={{ textAlign: "center" }}>{val}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </S.Wrapper>
  );
};

export default Main;
