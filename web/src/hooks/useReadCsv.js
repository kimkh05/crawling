import Papa from "papaparse";
import { useEffect, useState } from "react";

const useReadCsv = () => {
  const [value, setValue] = useState({});
  const getCsvFiles = () => {
    Papa.parse("../../../wanted.csv", {
      header: true,
      complete: (results) => {
        setValue(results);
      },
    });
  };
  useEffect(() => {
    getCsvFiles();
  }, []);
  return value;
};

export default useReadCsv;
