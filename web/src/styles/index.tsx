import { ThemeProvider } from "styled-components";
import { theme } from "./theme";
import { Global } from "./global";

interface PropsType {
  children: React.ReactNode;
}

export const StyleProvider = ({ children }: PropsType) => {
  return (
    <ThemeProvider theme={theme}>
      <Global />
      {children}
    </ThemeProvider>
  );
};
