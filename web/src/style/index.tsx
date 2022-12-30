import { ThemeProvider } from "styled-components";
import { Global } from "./global";
import { theme } from "./theme";

interface PropsType {
  children: React.ReactNode;
}

const StyleProvider = ({ children }: PropsType) => {
  return (
    <ThemeProvider theme={theme}>
      <Global />
      {children}
    </ThemeProvider>
  );
};

export default StyleProvider;
